# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1626 | 1413 | 1602 | 1680 | 1631 | 1468 | 1718 | 1501 |
| response time (ms), 99th percentile | 5187 | 4890 | 5161 | 5138 | 5056 | 4837 | 4899 | 4730 |
| time over the response line (% of samples) | 28.23 | 19.52 | 17.97 | 12.98 | 18.38 | 13.34 | 24.58 | 17.64 |
| failed requests (%) | 12.14 | 10.29 | 5.696 | 5.092 | 6.282 | 5.662 | 7.714 | 7.068 |
| HPA replicas, mean | 9.68 | 12.81 | 9.602 | 13.2 | 9.611 | 13.19 | 9.604 | 13.49 |
| pods started | 4.903 | 10.13 | 5.161 | 9.645 | 5.081 | 9.677 | 5.161 | 10.21 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 181.9 | 181.8 | 180 | 179.4 | 180.2 | 179.7 | 181.5 | 181.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.9 | 181.8 | 180 | 179.4 | 180.2 | 179.7 | 181.5 | 181.6 |
| CPU used with Omni's own (cores), mean | 2.176 | 2.163 | 1.956 | 1.957 | 1.953 | 1.962 | 2.112 | 2.121 |
| host CPU busy, the real machine under kind (%) | 64.44 | 64.39 | 58.06 | 58.29 | 58.13 | 58.4 | 62.61 | 63.18 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1626 | 1413 | -13.1% | -400.4 to -25.26 | GAIN |
| response time (ms), 99th percentile | 5187 | 4890 | -5.7% | -653.6 to +60.67 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 28.23 | 19.52 | -30.9% | -10.49 to -6.927 | GAIN |
| failed requests (%) | 12.14 | 10.29 | -15.2% | -2.619 to -1.082 | GAIN |
| HPA replicas, mean | 9.68 | 12.81 | +32.3% | +2.715 to +3.536 | power given |
| pods started | 4.903 | 10.13 | +106.6% | +4.69 to +5.762 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.733e-16 to +7.219e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.9 | 181.8 | -0.1% | -0.4214 to +0.1694 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.9 | 181.8 | -0.1% | -0.4214 to +0.1694 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.176 | 2.163 | -0.6% | -0.02409 to -0.002599 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.44 | 64.39 | -0.1% | -0.3419 to +0.2304 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.619e+05 to +8.623e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.147e-05 to -8.143e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1602 | 1680 | +4.9% | -119 to +274.9 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5161 | 5138 | -0.5% | -281.8 to +235.3 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 17.97 | 12.98 | -27.8% | -5.966 to -4.014 | GAIN |
| failed requests (%) | 5.696 | 5.092 | -10.6% | -0.9321 to -0.2749 | GAIN |
| HPA replicas, mean | 9.602 | 13.2 | +37.5% | +3.08 to +4.121 | power given |
| pods started | 5.161 | 9.645 | +86.9% | +3.766 to +5.202 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.109e-16 to +8.116e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180 | 179.4 | -0.3% | -0.9276 to -0.2238 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180 | 179.4 | -0.3% | -0.9276 to -0.2238 | GAIN |
| CPU used with Omni's own (cores), mean | 1.956 | 1.957 | +0.0% | -0.007507 to +0.009229 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.06 | 58.29 | +0.4% | +0.02001 to +0.4292 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1631 | 1468 | -10.0% | -351.2 to +24.55 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5056 | 4837 | -4.3% | -470.1 to +32.83 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 18.38 | 13.34 | -27.4% | -6.079 to -3.985 | GAIN |
| failed requests (%) | 6.282 | 5.662 | -9.9% | -1.009 to -0.2307 | GAIN |
| HPA replicas, mean | 9.611 | 13.19 | +37.3% | +3.076 to +4.089 | power given |
| pods started | 5.081 | 9.677 | +90.5% | +3.94 to +5.254 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.611e-16 to +2.032e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.2 | 179.7 | -0.3% | -0.7922 to -0.1806 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.2 | 179.7 | -0.3% | -0.7922 to -0.1806 | GAIN |
| CPU used with Omni's own (cores), mean | 1.953 | 1.962 | +0.4% | +0.0007206 to +0.01574 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.13 | 58.4 | +0.5% | +0.08415 to +0.4699 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1718 | 1501 | -12.6% | -348.5 to -84.48 | GAIN |
| response time (ms), 99th percentile | 4899 | 4730 | -3.4% | -474.1 to +136.9 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 24.58 | 17.64 | -28.2% | -8.204 to -5.679 | GAIN |
| failed requests (%) | 7.714 | 7.068 | -8.4% | -0.9563 to -0.336 | GAIN |
| HPA replicas, mean | 9.604 | 13.49 | +40.5% | +3.44 to +4.334 | power given |
| pods started | 5.161 | 10.21 | +97.8% | +4.488 to +5.608 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.661e-16 to +1.656e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.5 | 181.6 | +0.1% | -0.1515 to +0.4741 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.5 | 181.6 | +0.1% | -0.1515 to +0.4741 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.112 | 2.121 | +0.4% | +0.001403 to +0.01593 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.61 | 63.18 | +0.9% | +0.3727 to +0.7564 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
