# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1608 | 1506 | 1654 | 1577 | 2101 | 1989 | 1997 | 1820 |
| response time (ms), 99th percentile | 4658 | 5134 | 4750 | 4814 | 6003 | 6037 | 5340 | 5277 |
| time over the response line (% of samples) | 27.79 | 19.79 | 17.4 | 12.48 | 22.87 | 16.88 | 28.61 | 20.02 |
| failed requests (%) | 12.33 | 10.32 | 5.696 | 5.134 | 8.069 | 7.123 | 9.205 | 8.188 |
| HPA replicas, mean | 9.672 | 12.74 | 9.596 | 13.09 | 9.668 | 13.81 | 9.628 | 13.8 |
| pods started | 5.032 | 10.02 | 5.194 | 9.694 | 4.677 | 9.597 | 4.968 | 10.11 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 181.9 | 181.9 | 179.8 | 179.2 | 181.9 | 180.8 | 182.5 | 182.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.9 | 181.9 | 179.8 | 179.2 | 181.9 | 180.8 | 182.5 | 182.1 |
| CPU used with Omni's own (cores), mean | 2.178 | 2.169 | 1.929 | 1.933 | 2.107 | 2.112 | 2.201 | 2.2 |
| host CPU busy, the real machine under kind (%) | 64.54 | 64.7 | 57.4 | 57.65 | 62.42 | 62.68 | 65.34 | 65.83 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 99th percentile; organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1608 | 1506 | -6.3% | -283.6 to +79.86 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4658 | 5134 | +10.2% | +87.22 to +863.3 | LOSS |
| time over the response line (% of samples) | 27.79 | 19.79 | -28.8% | -9.695 to -6.303 | GAIN |
| failed requests (%) | 12.33 | 10.32 | -16.3% | -3.001 to -1.017 | GAIN |
| HPA replicas, mean | 9.672 | 12.74 | +31.7% | +2.643 to +3.493 | power given |
| pods started | 5.032 | 10.02 | +99.0% | +4.44 to +5.528 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.691e-16 to +1.686e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.9 | 181.9 | +0.0% | -0.2851 to +0.3349 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.9 | 181.9 | +0.0% | -0.2851 to +0.3349 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.178 | 2.169 | -0.4% | -0.01869 to +0.001156 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.54 | 64.7 | +0.2% | -0.08272 to +0.4032 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.62e+05 to +8.624e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.148e-05 to -8.145e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1654 | 1577 | -4.7% | -286.6 to +131 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4750 | 4814 | +1.3% | -203.9 to +331.4 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 17.4 | 12.48 | -28.3% | -5.872 to -3.973 | GAIN |
| failed requests (%) | 5.696 | 5.134 | -9.9% | -0.9039 to -0.2191 | GAIN |
| HPA replicas, mean | 9.596 | 13.09 | +36.5% | +2.967 to +4.03 | power given |
| pods started | 5.194 | 9.694 | +86.6% | +3.788 to +5.212 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.82e-16 to -2.354e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 179.2 | -0.3% | -0.9032 to -0.3196 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 179.2 | -0.3% | -0.9032 to -0.3196 | GAIN |
| CPU used with Omni's own (cores), mean | 1.929 | 1.933 | +0.2% | -0.002391 to +0.01141 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.4 | 57.65 | +0.4% | +0.05104 to +0.4497 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2101 | 1989 | -5.4% | -352.4 to +126.9 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6003 | 6037 | +0.6% | -294.7 to +363.5 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 22.87 | 16.88 | -26.2% | -6.856 to -5.131 | GAIN |
| failed requests (%) | 8.069 | 7.123 | -11.7% | -1.26 to -0.6313 | GAIN |
| HPA replicas, mean | 9.668 | 13.81 | +42.8% | +3.7 to +4.582 | power given |
| pods started | 4.677 | 9.597 | +105.2% | +4.336 to +5.502 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.589e-16 to -5.734e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.9 | 180.8 | -0.6% | -1.361 to -0.7333 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.9 | 180.8 | -0.6% | -1.361 to -0.7333 | GAIN |
| CPU used with Omni's own (cores), mean | 2.107 | 2.112 | +0.2% | -0.002678 to +0.01272 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.42 | 62.68 | +0.4% | +0.07049 to +0.4484 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1997 | 1820 | -8.9% | -361.6 to +6.862 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5340 | 5277 | -1.2% | -426.6 to +300.3 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 28.61 | 20.02 | -30.0% | -9.962 to -7.225 | GAIN |
| failed requests (%) | 9.205 | 8.188 | -11.1% | -1.374 to -0.6602 | GAIN |
| HPA replicas, mean | 9.628 | 13.8 | +43.3% | +3.749 to +4.588 | power given |
| pods started | 4.968 | 10.11 | +103.6% | +4.566 to +5.724 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003354 to +0.001088 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.5 | 182.1 | -0.2% | -0.6998 to -0.02553 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.5 | 182.1 | -0.2% | -0.726 to -0.04497 | GAIN |
| CPU used with Omni's own (cores), mean | 2.201 | 2.2 | -0.1% | -0.01196 to +0.008673 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.34 | 65.83 | +0.7% | +0.2262 to +0.742 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.377e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
