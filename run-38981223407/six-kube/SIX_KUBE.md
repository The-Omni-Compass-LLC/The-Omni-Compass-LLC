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
| response time (ms), 95th percentile | 2278 | 2894 | 2538 | 2638 | 2210 | 2452 | 3123 | 3568 | 3367 | 3767 | 2384 | 3042 |
| response time (ms), 99th percentile | 4438 | 5443 | 5377 | 5415 | 4823 | 5189 | 5536 | 6662 | 5808 | 6158 | 4923 | 5696 |
| time over the response line (% of samples) | 38.57 | 35.31 | 42.71 | 40.94 | 44.04 | 40.8 | 53.81 | 48.48 | 52.33 | 49.37 | 45.63 | 43.44 |
| failed requests (%) | 20.24 | 19.77 | 29.44 | 30.66 | 29.29 | 30.45 | 33.95 | 33.28 | 36.67 | 36.06 | 25.9 | 27.13 |
| HPA replicas, mean | 9.667 | 13.49 | 9.655 | 13.33 | 9.668 | 13.37 | 9.724 | 14.36 | 9.748 | 13.88 | 9.778 | 13.5 |
| pods started | 4.878 | 9.561 | 4.878 | 9.171 | 4.683 | 9.049 | 4.415 | 9.585 | 3.707 | 8 | 3.146 | 6.976 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.998 | 5.999 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 184.2 | 184.2 | 184.1 | 184.2 | 184.8 | 185.3 | 185.3 | 184.6 | 184.4 | 184.9 | 184.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 184.2 | 184.2 | 184.1 | 184.2 | 184.8 | 185.3 | 185.3 | 184.6 | 184.4 | 184.9 | 184.3 |
| CPU used with Omni's own (cores), mean | 2.335 | 2.351 | 2.351 | 2.361 | 2.383 | 2.403 | 2.474 | 2.495 | 2.392 | 2.418 | 2.408 | 2.435 |
| host CPU busy, the real machine under kind (%) | 68.39 | 69.73 | 70.07 | 70.74 | 70.85 | 71.97 | 72.76 | 74.26 | 71.45 | 73.52 | 72.22 | 75.47 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.002439 | 0.009756 | 0.002439 | 0.01463 | 0.004878 | 0.009756 | 0.002439 | 0.01463 | 0.1024 | 0.2073 | 0.1463 | 0.1854 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2278 | 2894 | +27.0% | +178.8 to +1052 | LOSS |
| response time (ms), 99th percentile | 4438 | 5443 | +22.6% | +457.2 to +1553 | LOSS |
| time over the response line (% of samples) | 38.57 | 35.31 | -8.4% | -4.943 to -1.565 | GAIN |
| failed requests (%) | 20.24 | 19.77 | -2.3% | -1.123 to +0.1825 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.667 | 13.49 | +39.5% | +3.195 to +4.443 | power given |
| pods started | 4.878 | 9.561 | +96.0% | +3.819 to +5.547 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.952e-16 to -5.473e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 184.2 | +0.2% | -0.02275 to +0.9361 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 184.2 | +0.2% | -0.02275 to +0.9361 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.335 | 2.351 | +0.7% | +0.009488 to +0.02257 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.39 | 69.73 | +2.0% | +1.073 to +1.606 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | LOSS |
| organism behind its window (s) | 0.002439 | 0.009756 | +300.0% | -0.003265 to +0.0179 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (failed requests (%); organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2538 | 2638 | +3.9% | -398.3 to +598 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5377 | 5415 | +0.7% | -492.8 to +569.3 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 42.71 | 40.94 | -4.1% | -2.853 to -0.6834 | GAIN |
| failed requests (%) | 29.44 | 30.66 | +4.2% | +0.3745 to +2.081 | LOSS |
| HPA replicas, mean | 9.655 | 13.33 | +38.0% | +2.931 to +4.413 | power given |
| pods started | 4.878 | 9.171 | +88.0% | +3.485 to +5.1 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.838e-16 to +3.704e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.1 | -0.0% | -0.5105 to +0.3819 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.1 | -0.0% | -0.5105 to +0.3819 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.351 | 2.361 | +0.4% | -0.002684 to +0.02201 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.07 | 70.74 | +1.0% | +0.2691 to +1.069 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | LOSS |
| organism behind its window (s) | 0.002439 | 0.01463 | +500.0% | -3.957e-05 to +0.02443 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), EVEN (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2210 | 2452 | +10.9% | -234 to +717.2 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4823 | 5189 | +7.6% | -171.7 to +905.1 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 44.04 | 40.8 | -7.3% | -4.524 to -1.939 | GAIN |
| failed requests (%) | 29.29 | 30.45 | +4.0% | +0.4641 to +1.874 | LOSS |
| HPA replicas, mean | 9.668 | 13.37 | +38.3% | +3.016 to +4.394 | power given |
| pods started | 4.683 | 9.049 | +93.2% | +3.525 to +5.206 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.491e-16 to +1.892e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.8 | +0.3% | +0.2687 to +0.8555 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.8 | +0.3% | +0.2687 to +0.8555 | power given |
| CPU used with Omni's own (cores), mean | 2.383 | 2.403 | +0.8% | +0.01292 to +0.02702 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.85 | 71.97 | +1.6% | +0.9105 to +1.314 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.004878 | 0.009756 | +100.0% | -0.00688 to +0.01664 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 99th percentile; organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3123 | 3568 | +14.2% | -67.42 to +956.6 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5536 | 6662 | +20.4% | +533.6 to +1720 | LOSS |
| time over the response line (% of samples) | 53.81 | 48.48 | -9.9% | -6.983 to -3.687 | GAIN |
| failed requests (%) | 33.95 | 33.28 | -2.0% | -1.679 to +0.3485 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.724 | 14.36 | +47.7% | +4.202 to +5.079 | power given |
| pods started | 4.415 | 9.585 | +117.1% | +4.544 to +5.798 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.006953 to +0.002255 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.3 | 185.3 | +0.0% | -0.389 to +0.5287 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.3 | 185.3 | +0.0% | -0.4372 to +0.4814 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.474 | 2.495 | +0.8% | +0.01462 to +0.0268 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.76 | 74.26 | +2.1% | +1.31 to +1.683 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | LOSS |
| organism behind its window (s) | 0.002439 | 0.01463 | +500.0% | -3.957e-05 to +0.02443 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3367 | 3767 | +11.9% | -64.36 to +865.1 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5808 | 6158 | +6.0% | -25.61 to +725.4 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 52.33 | 49.37 | -5.6% | -4.263 to -1.65 | GAIN |
| failed requests (%) | 36.67 | 36.06 | -1.7% | -1.712 to +0.4942 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.748 | 13.88 | +42.4% | +3.688 to +4.576 | power given |
| pods started | 3.707 | 8 | +115.8% | +3.604 to +4.981 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.0006745 to +0.00208 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 184.4 | -0.1% | -0.6215 to +0.1609 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.4 | -0.1% | -0.6147 to +0.1826 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.392 | 2.418 | +1.1% | +0.01209 to +0.04034 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.45 | 73.52 | +2.9% | +1.686 to +2.436 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.1024 | 0.2073 | +102.4% | +0.09127 to +0.1185 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%); organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 0

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2384 | 3042 | +27.6% | +292.3 to +1023 | LOSS |
| response time (ms), 99th percentile | 4923 | 5696 | +15.7% | +132.1 to +1414 | LOSS |
| time over the response line (% of samples) | 45.63 | 43.44 | -4.8% | -3.42 to -0.9618 | GAIN |
| failed requests (%) | 25.9 | 27.13 | +4.8% | +0.505 to +1.962 | LOSS |
| HPA replicas, mean | 9.778 | 13.5 | +38.1% | +3.299 to +4.148 | power given |
| pods started | 3.146 | 6.976 | +121.7% | +3.145 to +4.513 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.184e-16 to +2.285e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.9 | 184.3 | -0.3% | -0.8509 to -0.2442 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.9 | 184.3 | -0.3% | -0.8509 to -0.2442 | GAIN |
| CPU used with Omni's own (cores), mean | 2.408 | 2.435 | +1.1% | +0.02059 to +0.0339 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.22 | 75.47 | +4.5% | +3.085 to +3.419 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | LOSS |
| organism behind its window (s) | 0.1463 | 0.1854 | +26.7% | +0.01543 to +0.06261 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
