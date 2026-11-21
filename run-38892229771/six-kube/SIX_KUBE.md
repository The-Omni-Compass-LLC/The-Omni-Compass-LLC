# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1681 | 1576 | 1669 | 1582 | 1705 | 1697 | 1692 | 1548 |
| response time (ms), 99th percentile | 4869 | 5401 | 5421 | 5283 | 5622 | 5356 | 4589 | 4560 |
| time over the response line (% of samples) | 28.87 | 20.62 | 19.16 | 13.56 | 19.79 | 14.66 | 24.8 | 17.83 |
| failed requests (%) | 12.87 | 10.93 | 6.312 | 5.262 | 7.043 | 6.266 | 8.067 | 7.471 |
| HPA replicas, mean | 9.678 | 12.89 | 9.615 | 13.41 | 9.621 | 13.46 | 9.599 | 13.17 |
| pods started | 5.048 | 10.11 | 5.145 | 9.984 | 5.081 | 9.516 | 5 | 9.387 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 182.3 | 180.6 | 179.8 | 180.9 | 180 | 181.1 | 180.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 182.3 | 180.6 | 179.8 | 180.9 | 180 | 181.1 | 180.8 |
| CPU used with Omni's own (cores), mean | 2.198 | 2.193 | 2.001 | 2.001 | 2.013 | 2.022 | 2.07 | 2.074 |
| host CPU busy, the real machine under kind (%) | 64.98 | 65.21 | 59.35 | 59.53 | 59.8 | 60.07 | 61.35 | 61.96 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0.05161 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 99th percentile; organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1681 | 1576 | -6.3% | -247.5 to +36.47 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4869 | 5401 | +10.9% | +140.9 to +923 | LOSS |
| time over the response line (% of samples) | 28.87 | 20.62 | -28.6% | -9.817 to -6.684 | GAIN |
| failed requests (%) | 12.87 | 10.93 | -15.1% | -2.71 to -1.169 | GAIN |
| HPA replicas, mean | 9.678 | 12.89 | +33.2% | +2.763 to +3.664 | power given |
| pods started | 5.048 | 10.11 | +100.3% | +4.577 to +5.552 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.421e-16 to +4.103e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 182.3 | -0.0% | -0.4019 to +0.2772 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 182.3 | -0.0% | -0.4019 to +0.2772 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.198 | 2.193 | -0.2% | -0.01469 to +0.004184 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.98 | 65.21 | +0.4% | -0.03398 to +0.4956 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.621e+05 to +8.624e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.149e-05 to -8.145e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1669 | 1582 | -5.2% | -332.1 to +158.1 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5421 | 5283 | -2.5% | -435.9 to +159.6 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 19.16 | 13.56 | -29.2% | -6.607 to -4.59 | GAIN |
| failed requests (%) | 6.312 | 5.262 | -16.6% | -1.478 to -0.6216 | GAIN |
| HPA replicas, mean | 9.615 | 13.41 | +39.4% | +3.308 to +4.275 | power given |
| pods started | 5.145 | 9.984 | +94.0% | +4.206 to +5.472 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.597e-16 to +1.535e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 179.8 | -0.4% | -1.147 to -0.4254 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 179.8 | -0.4% | -1.147 to -0.4254 | GAIN |
| CPU used with Omni's own (cores), mean | 2.001 | 2.001 | -0.0% | -0.01035 to +0.01014 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.35 | 59.53 | +0.3% | -0.08735 to +0.4314 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1705 | 1697 | -0.4% | -265.3 to +250.2 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5622 | 5356 | -4.7% | -543.7 to +12.74 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 19.79 | 14.66 | -25.9% | -5.991 to -4.267 | GAIN |
| failed requests (%) | 7.043 | 6.266 | -11.0% | -1.114 to -0.4403 | GAIN |
| HPA replicas, mean | 9.621 | 13.46 | +39.9% | +3.331 to +4.34 | power given |
| pods started | 5.081 | 9.516 | +87.3% | +3.816 to +5.055 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.783e-16 to +2.497e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 180 | -0.5% | -1.222 to -0.5854 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 180 | -0.5% | -1.222 to -0.5854 | GAIN |
| CPU used with Omni's own (cores), mean | 2.013 | 2.022 | +0.4% | +0.002467 to +0.01561 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.8 | 60.07 | +0.5% | +0.1032 to +0.4498 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1692 | 1548 | -8.5% | -245.7 to -41.7 | GAIN |
| response time (ms), 99th percentile | 4589 | 4560 | -0.6% | -304.7 to +247.5 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 24.8 | 17.83 | -28.1% | -8.336 to -5.602 | GAIN |
| failed requests (%) | 8.067 | 7.471 | -7.4% | -0.8286 to -0.3628 | GAIN |
| HPA replicas, mean | 9.599 | 13.17 | +37.2% | +3.014 to +4.128 | power given |
| pods started | 5 | 9.387 | +87.7% | +3.641 to +5.134 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.853e-16 to -8.823e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 180.8 | -0.1% | -0.5842 to +0.08826 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 180.8 | -0.1% | -0.5842 to +0.08826 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.07 | 2.074 | +0.2% | -0.002935 to +0.01148 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.35 | 61.96 | +1.0% | +0.4179 to +0.7974 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | LOSS |
| organism behind its window (s) | 0.05161 | 0 | -100.0% | -0.1528 to +0.04955 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
