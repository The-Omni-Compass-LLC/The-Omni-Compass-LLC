# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1990 | 2082 | 2031 | 2925 | 2798 | 2894 | 2137 | 2195 | 2584 | 2926 | 3411 | 4881 | 2138 | 3677 |
| response time (ms), 99th percentile | 4263 | 4169 | 4295 | 5563 | 5806 | 5931 | 4160 | 4922 | 5128 | 5482 | 6165 | 7198 | 4198 | 5664 |
| time over the response line (% of samples) | 41.48 | 36.21 | 45.68 | 41.59 | 45.73 | 41.09 | 44.23 | 39.22 | 38.95 | 33.96 | 59.49 | 56.78 | 37.52 | 35.71 |
| failed requests (%) | 28.29 | 27.48 | 26.26 | 24.68 | 29.68 | 29.32 | 29.35 | 29.22 | 20.25 | 18.78 | 40.53 | 37.02 | 18.33 | 18.09 |
| HPA replicas, mean | 9.623 | 11.26 | 9.69 | 13.59 | 9.669 | 12.1 | 9.661 | 11.71 | 9.638 | 12.88 | 9.767 | 13.71 | 9.671 | 12.39 |
| pods started | 5.059 | 6.941 | 4.543 | 8.657 | 4.629 | 7.257 | 4.629 | 6.571 | 5.143 | 8.914 | 3.429 | 7.829 | 4.771 | 7.514 |
| worker nodes in service, mean | 5.998 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 183.9 | 184.4 | 184.9 | 184.7 | 184.8 | 183.7 | 184.5 | 183.7 | 184.3 | 185.4 | 185.9 | 183.4 | 183.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 183.9 | 184.4 | 184.9 | 184.7 | 184.8 | 183.7 | 184.5 | 183.7 | 184.3 | 185.4 | 185.9 | 183.4 | 183.5 |
| CPU used with Omni's own (cores), mean | 2.3 | 2.305 | 2.418 | 2.422 | 2.425 | 2.438 | 2.36 | 2.364 | 2.341 | 2.358 | 2.51 | 2.526 | 2.301 | 2.323 |
| host CPU busy, the real machine under kind (%) | 68 | 68.49 | 71.01 | 71.99 | 71.81 | 72.69 | 70.18 | 70.88 | 68.44 | 69.69 | 74.92 | 76.72 | 68.94 | 71.9 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0.005882 | 0.01714 | 0.002857 | 0.002857 | 0.008571 | 0.002857 | 0.02 | 0.01143 | 0.008571 | 0.1 | 0.2457 | 0.14 | 0.1971 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 4

34 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1990 | 2082 | +4.6% | -489.7 to +673.4 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4263 | 4169 | -2.2% | -787.9 to +601.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 41.48 | 36.21 | -12.7% | -7.066 to -3.474 | GAIN |
| failed requests (%) | 28.29 | 27.48 | -2.8% | -2.008 to +0.3982 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.623 | 11.26 | +17.0% | +0.854 to +2.415 | power given |
| pods started | 5.059 | 6.941 | +37.2% | +0.8849 to +2.88 | power given |
| worker nodes in service, mean | 5.998 | 6 | +0.0% | -0.001589 to +0.00466 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 183.9 | +0.3% | +0.09139 to +0.9263 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 183.9 | +0.3% | +0.1287 to +0.9515 | power given |
| CPU used with Omni's own (cores), mean | 2.3 | 2.305 | +0.2% | -0.004665 to +0.01499 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68 | 68.49 | +0.7% | +0.1496 to +0.831 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0.005882 | +0.00588 | -0.002453 to +0.01422 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 0

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2031 | 2925 | +44.0% | +403.2 to +1385 | LOSS |
| response time (ms), 99th percentile | 4295 | 5563 | +29.5% | +508.3 to +2028 | LOSS |
| time over the response line (% of samples) | 45.68 | 41.59 | -9.0% | -5.624 to -2.561 | GAIN |
| failed requests (%) | 26.26 | 24.68 | -6.0% | -2.632 to -0.5399 | GAIN |
| HPA replicas, mean | 9.69 | 13.59 | +40.3% | +3.155 to +4.645 | power given |
| pods started | 4.543 | 8.657 | +90.6% | +3.18 to +5.049 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.25e-16 to +4.25e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.9 | +0.3% | +0.04247 to +1.027 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.9 | +0.3% | +0.04247 to +1.027 | power given |
| CPU used with Omni's own (cores), mean | 2.418 | 2.422 | +0.2% | -0.008376 to +0.01766 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.01 | 71.99 | +1.4% | +0.5092 to +1.446 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01714 | 0.002857 | -83.3% | -0.02905 to +0.0004825 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2798 | 2894 | +3.4% | -573.5 to +765.2 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5806 | 5931 | +2.1% | -471.8 to +721.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 45.73 | 41.09 | -10.1% | -6.107 to -3.167 | GAIN |
| failed requests (%) | 29.68 | 29.32 | -1.2% | -1.359 to +0.6397 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.669 | 12.1 | +25.1% | +1.62 to +3.236 | power given |
| pods started | 4.629 | 7.257 | +56.8% | +1.636 to +3.622 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.816e-16 to +7.398e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 184.8 | +0.0% | -0.4345 to +0.6139 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 184.8 | +0.0% | -0.4345 to +0.6139 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.425 | 2.438 | +0.5% | +0.001272 to +0.02336 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.81 | 72.69 | +1.2% | +0.5842 to +1.169 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.002857 | 0.008571 | +200.0% | -0.005897 to +0.01733 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2137 | 2195 | +2.7% | -250.5 to +366.5 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4160 | 4922 | +18.3% | +212.9 to +1312 | LOSS |
| time over the response line (% of samples) | 44.23 | 39.22 | -11.3% | -6.758 to -3.271 | GAIN |
| failed requests (%) | 29.35 | 29.22 | -0.4% | -0.9488 to +0.6949 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.661 | 11.71 | +21.2% | +1.19 to +2.912 | power given |
| pods started | 4.629 | 6.571 | +42.0% | +0.7827 to +3.103 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.8e-17 to +7.078e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 184.5 | +0.4% | +0.3846 to +1.121 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 184.5 | +0.4% | +0.3846 to +1.121 | power given |
| CPU used with Omni's own (cores), mean | 2.36 | 2.364 | +0.1% | -0.006814 to +0.01335 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.18 | 70.88 | +1.0% | +0.3775 to +1.017 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.002857 | 0.02 | +600.0% | +0.00159 to +0.0327 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2584 | 2926 | +13.2% | -230.4 to +913.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5128 | 5482 | +6.9% | -136.3 to +844.6 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 38.95 | 33.96 | -12.8% | -6.585 to -3.394 | GAIN |
| failed requests (%) | 20.25 | 18.78 | -7.3% | -2.588 to -0.3603 | GAIN |
| HPA replicas, mean | 9.638 | 12.88 | +33.6% | +2.43 to +4.049 | power given |
| pods started | 5.143 | 8.914 | +73.3% | +2.66 to +4.883 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.886e-16 to +7.953e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 184.3 | +0.3% | +0.1737 to +1.05 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 184.3 | +0.3% | +0.1737 to +1.05 | power given |
| CPU used with Omni's own (cores), mean | 2.341 | 2.358 | +0.7% | +0.007702 to +0.0272 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.44 | 69.69 | +1.8% | +0.9944 to +1.501 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.01143 | 0.008571 | -25.0% | -0.01599 to +0.01028 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 0

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3411 | 4881 | +43.1% | +741.4 to +2198 | LOSS |
| response time (ms), 99th percentile | 6165 | 7198 | +16.8% | +252.5 to +1814 | LOSS |
| time over the response line (% of samples) | 59.49 | 56.78 | -4.6% | -4.268 to -1.156 | GAIN |
| failed requests (%) | 40.53 | 37.02 | -8.7% | -5.169 to -1.852 | GAIN |
| HPA replicas, mean | 9.767 | 13.71 | +40.3% | +3.337 to +4.542 | power given |
| pods started | 3.429 | 7.829 | +128.3% | +3.479 to +5.321 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.773e-16 to +3.773e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 185.4 | 185.9 | +0.3% | +0.04194 to +0.95 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.4 | 185.9 | +0.3% | +0.04194 to +0.95 | power given |
| CPU used with Omni's own (cores), mean | 2.51 | 2.526 | +0.7% | +0.01013 to +0.02301 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.92 | 76.72 | +2.4% | +1.617 to +1.998 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1 | 0.2457 | +145.7% | +0.112 to +0.1794 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2138 | 3677 | +72.0% | +899.5 to +2179 | LOSS |
| response time (ms), 99th percentile | 4198 | 5664 | +34.9% | +623.7 to +2308 | LOSS |
| time over the response line (% of samples) | 37.52 | 35.71 | -4.8% | -3.251 to -0.3712 | GAIN |
| failed requests (%) | 18.33 | 18.09 | -1.3% | -1.214 to +0.74 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.671 | 12.39 | +28.1% | +1.972 to +3.458 | power given |
| pods started | 4.771 | 7.514 | +57.5% | +1.837 to +3.649 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.155e-16 to +2.095e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 183.5 | +0.0% | -0.3278 to +0.4952 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 183.5 | +0.0% | -0.3278 to +0.4952 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.301 | 2.323 | +1.0% | +0.0103 to +0.03464 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.94 | 71.9 | +4.3% | +2.616 to +3.305 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.14 | 0.1971 | +40.8% | +0.02916 to +0.08513 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
