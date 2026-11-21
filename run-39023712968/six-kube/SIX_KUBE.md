# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1774 | 1718 | 2056 | 1971 | 1919 | 1715 | 1543 | 1339 |
| response time (ms), 99th percentile | 5145 | 5279 | 6079 | 6128 | 5876 | 5580 | 4165 | 4227 |
| time over the response line (% of samples) | 29.08 | 19.91 | 21.65 | 16.16 | 19.75 | 14.83 | 22.3 | 16.02 |
| failed requests (%) | 12.97 | 10.29 | 7.508 | 6.689 | 6.475 | 5.99 | 7.003 | 6.467 |
| HPA replicas, mean | 9.671 | 13.04 | 9.651 | 13.81 | 9.619 | 13.63 | 9.564 | 13.15 |
| pods started | 5.097 | 10.13 | 4.855 | 9.694 | 5.113 | 9.839 | 5.371 | 9.71 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 182.4 | 182.1 | 181.6 | 180.6 | 180.9 | 180 | 180.6 | 180.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.4 | 182.1 | 181.6 | 180.6 | 180.9 | 180 | 180.6 | 180.4 |
| CPU used with Omni's own (cores), mean | 2.2 | 2.186 | 2.09 | 2.097 | 2.022 | 2.029 | 2.03 | 2.035 |
| host CPU busy, the real machine under kind (%) | 65.02 | 65.02 | 61.88 | 62.18 | 59.98 | 60.27 | 60.18 | 60.67 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1774 | 1718 | -3.1% | -252.1 to +140.7 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5145 | 5279 | +2.6% | -296.4 to +565.4 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 29.08 | 19.91 | -31.5% | -10.96 to -7.386 | GAIN |
| failed requests (%) | 12.97 | 10.29 | -20.7% | -3.92 to -1.445 | GAIN |
| HPA replicas, mean | 9.671 | 13.04 | +34.9% | +2.955 to +3.79 | power given |
| pods started | 5.097 | 10.13 | +98.7% | +4.436 to +5.628 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.775e-16 to -9.526e-18 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.4 | 182.1 | -0.2% | -0.6582 to +0.05012 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.4 | 182.1 | -0.2% | -0.6582 to +0.05012 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.2 | 2.186 | -0.6% | -0.02446 to -0.003956 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.02 | 65.02 | +0.0% | -0.3045 to +0.3071 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.62e+05 to +8.623e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.148e-05 to -8.144e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2056 | 1971 | -4.1% | -336 to +166.7 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6079 | 6128 | +0.8% | -246.4 to +344.1 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 21.65 | 16.16 | -25.4% | -6.342 to -4.643 | GAIN |
| failed requests (%) | 7.508 | 6.689 | -10.9% | -1.158 to -0.4786 | GAIN |
| HPA replicas, mean | 9.651 | 13.81 | +43.1% | +3.71 to +4.614 | power given |
| pods started | 4.855 | 9.694 | +99.7% | +4.279 to +5.398 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.624e-16 to +3.997e-18 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.6 | 180.6 | -0.6% | -1.379 to -0.7465 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.6 | 180.6 | -0.6% | -1.379 to -0.7465 | GAIN |
| CPU used with Omni's own (cores), mean | 2.09 | 2.097 | +0.3% | +0.000268 to +0.01335 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.88 | 62.18 | +0.5% | +0.1143 to +0.4868 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.245e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 7 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 0

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1919 | 1715 | -10.7% | -377 to -31.88 | GAIN |
| response time (ms), 99th percentile | 5876 | 5580 | -5.0% | -565.9 to -25.94 | GAIN |
| time over the response line (% of samples) | 19.75 | 14.83 | -24.9% | -5.709 to -4.136 | GAIN |
| failed requests (%) | 6.475 | 5.99 | -7.5% | -0.7516 to -0.2199 | GAIN |
| HPA replicas, mean | 9.619 | 13.63 | +41.7% | +3.533 to +4.491 | power given |
| pods started | 5.113 | 9.839 | +92.4% | +4.104 to +5.347 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.639e-16 to +2.206e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 180 | -0.5% | -1.226 to -0.6191 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 180 | -0.5% | -1.226 to -0.6191 | GAIN |
| CPU used with Omni's own (cores), mean | 2.022 | 2.029 | +0.4% | -0.0008428 to +0.01635 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.98 | 60.27 | +0.5% | +0.06504 to +0.5258 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1543 | 1339 | -13.2% | -309.1 to -98.53 | GAIN |
| response time (ms), 99th percentile | 4165 | 4227 | +1.5% | -262.4 to +384.7 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 22.3 | 16.02 | -28.2% | -7.538 to -5.02 | GAIN |
| failed requests (%) | 7.003 | 6.467 | -7.6% | -0.7528 to -0.3185 | GAIN |
| HPA replicas, mean | 9.564 | 13.15 | +37.5% | +3.05 to +4.128 | power given |
| pods started | 5.371 | 9.71 | +80.8% | +3.695 to +4.982 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.858e-16 to +3.004e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 180.4 | -0.1% | -0.5025 to +0.08696 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 180.4 | -0.1% | -0.5025 to +0.08696 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.03 | 2.035 | +0.3% | -0.00177 to +0.01206 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.18 | 60.67 | +0.8% | +0.3 to +0.6889 | shown, not judged |
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
