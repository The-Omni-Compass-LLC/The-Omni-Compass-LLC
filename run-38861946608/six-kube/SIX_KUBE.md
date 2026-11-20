# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1406 | 1212 | 1378 | 1372 | 1734 | 1538 | 1967 | 1739 | 1487 | 1555 |
| response time (ms), 99th percentile | 4404 | 4369 | 4216 | 4163 | 5272 | 4893 | 5334 | 5330 | 4456 | 4684 |
| time over the response line (% of samples) | 23.65 | 16.9 | 14.74 | 10.89 | 18.58 | 13.65 | 29.64 | 21.65 | 25.75 | 18.69 |
| failed requests (%) | 10.35 | 8.885 | 4.831 | 4.292 | 6.291 | 5.878 | 9.706 | 8.876 | 11.66 | 9.93 |
| HPA replicas, mean | 9.627 | 12.1 | 9.55 | 12.68 | 9.603 | 13.04 | 9.647 | 13.96 | 9.66 | 12.68 |
| pods started | 5.24 | 9.92 | 5.7 | 9.64 | 5.08 | 9.46 | 4.84 | 10.12 | 4.98 | 10.42 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 180.4 | 179 | 178.3 | 180.2 | 179.3 | 182.5 | 182.6 | 181.2 | 181.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 180.4 | 179 | 178.3 | 180.2 | 179.3 | 182.5 | 182.6 | 181.2 | 181.4 |
| CPU used with Omni's own (cores), mean | 2.038 | 2.034 | 1.845 | 1.843 | 1.956 | 1.961 | 2.23 | 2.234 | 2.124 | 2.118 |
| host CPU busy, the real machine under kind (%) | 60.97 | 61.05 | 54.97 | 55.15 | 58.18 | 58.4 | 65.95 | 66.52 | 63.08 | 63.32 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.401 | 2.345 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.002 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1406 | 1212 | -13.8% | -335.4 to -53.23 | GAIN |
| response time (ms), 99th percentile | 4404 | 4369 | -0.8% | -376 to +306.1 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 23.65 | 16.9 | -28.5% | -8.453 to -5.052 | GAIN |
| failed requests (%) | 10.35 | 8.885 | -14.2% | -2.056 to -0.8786 | GAIN |
| HPA replicas, mean | 9.627 | 12.1 | +25.7% | +1.919 to +3.025 | power given |
| pods started | 5.24 | 9.92 | +89.3% | +3.993 to +5.367 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.197e-16 to +2.066e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 180.4 | -0.1% | -0.4632 to +0.1615 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 180.4 | -0.1% | -0.4632 to +0.1615 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.038 | 2.034 | -0.2% | -0.01321 to +0.005263 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.97 | 61.05 | +0.1% | -0.1744 to +0.3344 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.62e+05 to +8.624e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.148e-05 to -8.144e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1378 | 1372 | -0.4% | -226.4 to +215.4 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4216 | 4163 | -1.2% | -371.4 to +266.7 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 14.74 | 10.89 | -26.1% | -4.793 to -2.914 | GAIN |
| failed requests (%) | 4.831 | 4.292 | -11.2% | -0.9225 to -0.1558 | GAIN |
| HPA replicas, mean | 9.55 | 12.68 | +32.7% | +2.493 to +3.761 | power given |
| pods started | 5.7 | 9.64 | +69.1% | +3.135 to +4.745 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.02e-16 to +5.639e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179 | 178.3 | -0.4% | -1.016 to -0.3351 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179 | 178.3 | -0.4% | -1.016 to -0.3351 | GAIN |
| CPU used with Omni's own (cores), mean | 1.845 | 1.843 | -0.1% | -0.009759 to +0.006479 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.97 | 55.15 | +0.3% | -0.06895 to +0.4179 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 6 (response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 1

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1734 | 1538 | -11.3% | -444.4 to +52.39 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5272 | 4893 | -7.2% | -658.4 to -99.44 | GAIN |
| time over the response line (% of samples) | 18.58 | 13.65 | -26.5% | -5.944 to -3.901 | GAIN |
| failed requests (%) | 6.291 | 5.878 | -6.6% | -0.7456 to -0.0806 | GAIN |
| HPA replicas, mean | 9.603 | 13.04 | +35.8% | +2.851 to +4.03 | power given |
| pods started | 5.08 | 9.46 | +86.2% | +3.533 to +5.227 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.2e-16 to -9.711e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.2 | 179.3 | -0.5% | -1.249 to -0.5067 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.2 | 179.3 | -0.5% | -1.249 to -0.5067 | GAIN |
| CPU used with Omni's own (cores), mean | 1.956 | 1.961 | +0.3% | -0.003353 to +0.01339 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.18 | 58.4 | +0.4% | +0.02456 to +0.4272 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1967 | 1739 | -11.6% | -375.7 to -80.08 | GAIN |
| response time (ms), 99th percentile | 5334 | 5330 | -0.1% | -334.4 to +327.9 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 29.64 | 21.65 | -27.0% | -9.31 to -6.67 | GAIN |
| failed requests (%) | 9.706 | 8.876 | -8.6% | -1.087 to -0.5727 | GAIN |
| HPA replicas, mean | 9.647 | 13.96 | +44.7% | +3.844 to +4.774 | power given |
| pods started | 4.84 | 10.12 | +109.1% | +4.669 to +5.891 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.375e-16 to +6.903e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.5 | 182.6 | +0.1% | -0.1943 to +0.5463 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.5 | 182.6 | +0.1% | -0.1943 to +0.5463 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.23 | 2.234 | +0.1% | -0.002796 to +0.009109 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.95 | 66.52 | +0.9% | +0.3986 to +0.7453 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1487 | 1555 | +4.6% | -134.4 to +271.6 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4456 | 4684 | +5.1% | -177.6 to +634.7 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 25.75 | 18.69 | -27.4% | -8.909 to -5.203 | GAIN |
| failed requests (%) | 11.66 | 9.93 | -14.9% | -2.524 to -0.9439 | GAIN |
| HPA replicas, mean | 9.66 | 12.68 | +31.2% | +2.522 to +3.514 | power given |
| pods started | 4.98 | 10.42 | +109.2% | +4.729 to +6.151 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.461e-16 to +1.619e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.2 | 181.4 | +0.1% | -0.04511 to +0.5508 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.2 | 181.4 | +0.1% | -0.04511 to +0.5508 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.124 | 2.118 | -0.3% | -0.0168 to +0.004101 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.08 | 63.32 | +0.4% | -0.05808 to +0.5402 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.002 | +0.002 | -0.00192 to +0.00592 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
