# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2913 | 3988 | 3115 | 4463 | 1988 | 2930 | 3579 | 4547 | 3726 | 3834 | 1316 | 1944 |
| response time (ms), 99th percentile | 5671 | 7334 | 6228 | 7922 | 3921 | 5925 | 6438 | 7000 | 6034 | 6376 | 3166 | 3604 |
| time over the response line (% of samples) | 46.53 | 42.28 | 59.21 | 57.87 | 46.6 | 45.29 | 52.24 | 48.99 | 45.46 | 40.67 | 32.4 | 29.68 |
| failed requests (%) | 25.14 | 22.67 | 40.41 | 40.76 | 31.9 | 33.23 | 30.57 | 30.87 | 25.74 | 24.87 | 19.32 | 20.01 |
| HPA replicas, mean | 9.702 | 14.08 | 9.76 | 15.04 | 9.68 | 13.92 | 9.663 | 13.21 | 9.69 | 13.2 | 9.708 | 12.23 |
| pods started | 4.75 | 9.25 | 4.125 | 9.375 | 4.75 | 10.62 | 4.875 | 9.25 | 4.5 | 8.125 | 4 | 6.625 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 185 | 184.8 | 186.3 | 185.6 | 184 | 184.6 | 185 | 185.7 | 183.9 | 184.1 | 182.6 | 181.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185 | 184.8 | 186.3 | 185.6 | 184 | 184.6 | 185 | 185.7 | 183.9 | 184.1 | 182.6 | 181.3 |
| CPU used with Omni's own (cores), mean | 2.462 | 2.476 | 2.557 | 2.576 | 2.345 | 2.374 | 2.469 | 2.487 | 2.375 | 2.387 | 2.163 | 2.176 |
| host CPU busy, the real machine under kind (%) | 72.2 | 73.48 | 76.48 | 77.7 | 70.09 | 71.42 | 72.06 | 73.36 | 70.25 | 71.95 | 64.92 | 67.49 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0 | 0.0125 | 0.0125 | 0.0125 | 0.0125 | 0.0125 | 0.0875 | 0.2 | 0.1125 | 2.737 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2913 | 3988 | +36.9% | +108 to +2044 | LOSS |
| response time (ms), 99th percentile | 5671 | 7334 | +29.3% | +47 to +3279 | LOSS |
| time over the response line (% of samples) | 46.53 | 42.28 | -9.1% | -7.302 to -1.19 | GAIN |
| failed requests (%) | 25.14 | 22.67 | -9.8% | -5.143 to +0.2062 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.702 | 14.08 | +45.1% | +2.874 to +5.875 | power given |
| pods started | 4.75 | 9.25 | +94.7% | +2.404 to +6.596 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.97e-16 to +3.97e-16 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 185 | 184.8 | -0.1% | -1.616 to +1.2 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185 | 184.8 | -0.1% | -1.616 to +1.2 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.462 | 2.476 | +0.6% | +0.004664 to +0.02317 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.2 | 73.48 | +1.8% | +1.055 to +1.511 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3115 | 4463 | +43.3% | +420.1 to +2275 | LOSS |
| response time (ms), 99th percentile | 6228 | 7922 | +27.2% | +284 to +3103 | LOSS |
| time over the response line (% of samples) | 59.21 | 57.87 | -2.3% | -4.472 to +1.796 | EVEN, inside the noise (cut) |
| failed requests (%) | 40.41 | 40.76 | +0.9% | -0.9904 to +1.691 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.76 | 15.04 | +54.1% | +4.864 to +5.689 | power given |
| pods started | 4.125 | 9.375 | +127.3% | +4.006 to +6.494 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.467e-16 to +9.908e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.3 | 185.6 | -0.4% | -1.828 to +0.4262 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.3 | 185.6 | -0.4% | -1.828 to +0.4262 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.557 | 2.576 | +0.7% | +0.008786 to +0.0285 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.48 | 77.7 | +1.6% | +1.063 to +1.364 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | LOSS |
| organism behind its window (s) | 0 | 0.0125 | +0.0125 | -0.01706 to +0.04206 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1988 | 2930 | +47.4% | -148.6 to +2033 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 3921 | 5925 | +51.1% | +270.6 to +3738 | LOSS |
| time over the response line (% of samples) | 46.6 | 45.29 | -2.8% | -4.589 to +1.974 | EVEN, inside the noise (cut) |
| failed requests (%) | 31.9 | 33.23 | +4.2% | -0.003407 to +2.662 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.68 | 13.92 | +43.8% | +2.439 to +6.034 | power given |
| pods started | 4.75 | 10.62 | +123.7% | +4.577 to +7.173 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.658e-16 to +1.217e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.6 | +0.3% | -0.5004 to +1.583 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.6 | +0.3% | -0.5004 to +1.583 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.345 | 2.374 | +1.3% | -0.001033 to +0.06002 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.09 | 71.42 | +1.9% | +0.5828 to +2.083 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.0125 | 0.0125 | +0.0% | -0.04469 to +0.04469 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 6

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3579 | 4547 | +27.0% | -525.6 to +2461 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6438 | 7000 | +8.7% | -1295 to +2419 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 52.24 | 48.99 | -6.2% | -11.35 to +4.835 | EVEN, inside the noise (cut) |
| failed requests (%) | 30.57 | 30.87 | +1.0% | -1.671 to +2.269 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.663 | 13.21 | +36.7% | +1.671 to +5.413 | power given |
| pods started | 4.875 | 9.25 | +89.7% | +1.889 to +6.861 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.25e-16 to +8.47e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185 | 185.7 | +0.4% | -0.4129 to +1.848 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185 | 185.7 | +0.4% | -0.4129 to +1.848 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.469 | 2.487 | +0.7% | +0.001347 to +0.03432 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.06 | 73.36 | +1.8% | +0.9721 to +1.629 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | LOSS |
| organism behind its window (s) | 0.0125 | 0.0125 | +0.0% | -0.04469 to +0.04469 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3726 | 3834 | +2.9% | -647.5 to +863.4 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6034 | 6376 | +5.7% | -533 to +1215 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 45.46 | 40.67 | -10.5% | -8.338 to -1.251 | GAIN |
| failed requests (%) | 25.74 | 24.87 | -3.4% | -3.123 to +1.388 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.69 | 13.2 | +36.3% | +1.631 to +5.397 | power given |
| pods started | 4.5 | 8.125 | +80.6% | +1.06 to +6.19 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.416e-15 to +5.283e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 184.1 | +0.1% | -0.6509 to +1.175 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 184.1 | +0.1% | -0.6509 to +1.175 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.375 | 2.387 | +0.5% | -0.001739 to +0.02536 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.25 | 71.95 | +2.4% | +1.354 to +2.053 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.0875 | 0.2 | +128.6% | +0.08294 to +0.1421 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 6

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1316 | 1944 | +47.8% | -353.6 to +1610 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 3166 | 3604 | +13.8% | -353.2 to +1229 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 32.4 | 29.68 | -8.4% | -6.827 to +1.372 | EVEN, inside the noise (cut) |
| failed requests (%) | 19.32 | 20.01 | +3.6% | -1.099 to +2.482 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.708 | 12.23 | +26.0% | +0.7241 to +4.33 | power given |
| pods started | 4 | 6.625 | +65.6% | +0.4383 to +4.812 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.27e-16 to +1.437e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.6 | 181.3 | -0.7% | -4.466 to +1.737 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.6 | 181.3 | -0.7% | -4.466 to +1.737 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.163 | 2.176 | +0.6% | -0.01148 to +0.0384 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.92 | 67.49 | +4.0% | +1.309 to +3.821 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | LOSS |
| organism behind its window (s) | 0.1125 | 2.737 | +2333.3% | -3.414 to +8.664 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
