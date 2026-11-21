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
| response time (ms), 95th percentile | 3185 | 3838 | 2446 | 2486 | 2350 | 2826 | 2908 | 3274 | 2781 | 3718 | 2253 | 2744 |
| response time (ms), 99th percentile | 5757 | 6646 | 4737 | 5047 | 4620 | 5056 | 5066 | 5609 | 5431 | 5829 | 4717 | 5649 |
| time over the response line (% of samples) | 49.37 | 45.18 | 38.81 | 36.15 | 39.08 | 36.92 | 46.67 | 41.78 | 48.49 | 44.95 | 43.02 | 41.32 |
| failed requests (%) | 26.33 | 26.1 | 26.26 | 26.1 | 25.86 | 26.17 | 28.84 | 27.57 | 33.31 | 33.16 | 23.71 | 25.31 |
| HPA replicas, mean | 9.707 | 14.33 | 9.626 | 12.88 | 9.629 | 13.16 | 9.667 | 13.73 | 9.738 | 13.81 | 9.773 | 13.4 |
| pods started | 4.732 | 9.951 | 5.098 | 9.024 | 5.024 | 9.195 | 5.024 | 9.488 | 3.829 | 7.976 | 3.293 | 6.927 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 185.3 | 185.6 | 183.2 | 183.3 | 183.5 | 183.6 | 184.3 | 184.1 | 184.3 | 184 | 184.4 | 184.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.3 | 185.6 | 183.2 | 183.3 | 183.5 | 183.6 | 184.3 | 184.1 | 184.3 | 184 | 184.4 | 184.6 |
| CPU used with Omni's own (cores), mean | 2.506 | 2.524 | 2.277 | 2.298 | 2.307 | 2.326 | 2.368 | 2.378 | 2.373 | 2.394 | 2.39 | 2.425 |
| host CPU busy, the real machine under kind (%) | 73.27 | 74.74 | 67.49 | 68.49 | 68.46 | 69.67 | 69.55 | 70.73 | 70.89 | 72.73 | 71.73 | 75.28 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.01707 | 0.02683 | 0.0122 | 0.009756 | 0.002439 | 0.01463 | 0.009756 | 0.009756 | 0.09512 | 0.2024 | 0.1415 | 0.1756 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3185 | 3838 | +20.5% | +107.8 to +1198 | LOSS |
| response time (ms), 99th percentile | 5757 | 6646 | +15.4% | +282.8 to +1494 | LOSS |
| time over the response line (% of samples) | 49.37 | 45.18 | -8.5% | -5.709 to -2.654 | GAIN |
| failed requests (%) | 26.33 | 26.1 | -0.9% | -1.09 to +0.6302 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.707 | 14.33 | +47.6% | +4.245 to +4.993 | power given |
| pods started | 4.732 | 9.951 | +110.3% | +4.674 to +5.765 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.127e-16 to +4.159e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.3 | 185.6 | +0.1% | -0.2695 to +0.7192 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.3 | 185.6 | +0.1% | -0.2695 to +0.7192 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.506 | 2.524 | +0.7% | +0.012 to +0.02393 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.27 | 74.74 | +2.0% | +1.298 to +1.659 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | LOSS |
| organism behind its window (s) | 0.01707 | 0.02683 | +57.1% | -0.008099 to +0.02761 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2446 | 2486 | +1.7% | -379.3 to +460.8 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4737 | 5047 | +6.5% | -201.7 to +821.4 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 38.81 | 36.15 | -6.9% | -3.793 to -1.524 | GAIN |
| failed requests (%) | 26.26 | 26.1 | -0.6% | -1.285 to +0.949 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.626 | 12.88 | +33.8% | +2.501 to +4.014 | power given |
| pods started | 5.098 | 9.024 | +77.0% | +3.099 to +4.755 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.635e-16 to +7.357e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.2 | 183.3 | +0.0% | -0.3121 to +0.4735 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.2 | 183.3 | +0.0% | -0.3121 to +0.4735 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.277 | 2.298 | +0.9% | +0.01405 to +0.02754 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.49 | 68.49 | +1.5% | +0.802 to +1.194 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | LOSS |
| organism behind its window (s) | 0.0122 | 0.009756 | -20.0% | -0.01522 to +0.01034 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2350 | 2826 | +20.3% | -39.56 to +991.9 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4620 | 5056 | +9.4% | -206.7 to +1079 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 39.08 | 36.92 | -5.5% | -3.218 to -1.108 | GAIN |
| failed requests (%) | 25.86 | 26.17 | +1.2% | -0.5998 to +1.205 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.629 | 13.16 | +36.7% | +2.807 to +4.265 | power given |
| pods started | 5.024 | 9.195 | +83.0% | +3.276 to +5.066 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.589e-16 to +3.889e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 183.6 | +0.0% | -0.4249 to +0.4773 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 183.6 | +0.0% | -0.4249 to +0.4773 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.307 | 2.326 | +0.8% | +0.003647 to +0.03499 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.46 | 69.67 | +1.8% | +0.7939 to +1.622 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.002439 | 0.01463 | +500.0% | -3.957e-05 to +0.02443 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 99th percentile; organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2908 | 3274 | +12.6% | -170.2 to +902.8 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5066 | 5609 | +10.7% | +28.9 to +1059 | LOSS |
| time over the response line (% of samples) | 46.67 | 41.78 | -10.5% | -6.809 to -2.956 | GAIN |
| failed requests (%) | 28.84 | 27.57 | -4.4% | -2.464 to -0.08374 | GAIN |
| HPA replicas, mean | 9.667 | 13.73 | +42.0% | +3.423 to +4.703 | power given |
| pods started | 5.024 | 9.488 | +88.8% | +3.695 to +5.232 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.664e-16 to +5.13e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.1 | -0.1% | -0.6641 to +0.1746 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.1 | -0.1% | -0.6641 to +0.1746 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.368 | 2.378 | +0.4% | -7.153e-05 to +0.02076 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.55 | 70.73 | +1.7% | +0.8653 to +1.483 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | LOSS |
| organism behind its window (s) | 0.009756 | 0.009756 | +0.0% | -0.01369 to +0.01369 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2781 | 3718 | +33.7% | +362.8 to +1512 | LOSS |
| response time (ms), 99th percentile | 5431 | 5829 | +7.3% | -183.4 to +978.9 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 48.49 | 44.95 | -7.3% | -4.837 to -2.246 | GAIN |
| failed requests (%) | 33.31 | 33.16 | -0.4% | -1.012 to +0.7299 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.738 | 13.81 | +41.8% | +3.577 to +4.561 | power given |
| pods started | 3.829 | 7.976 | +108.3% | +3.536 to +4.757 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.929e-16 to +1.163e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184 | -0.1% | -0.5954 to +0.05398 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184 | -0.1% | -0.5954 to +0.05398 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.373 | 2.394 | +0.9% | +0.009267 to +0.03206 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.89 | 72.73 | +2.6% | +1.559 to +2.123 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.09512 | 0.2024 | +112.8% | +0.09925 to +0.1154 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%); organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2253 | 2744 | +21.8% | +160.5 to +820.6 | LOSS |
| response time (ms), 99th percentile | 4717 | 5649 | +19.8% | +317.5 to +1547 | LOSS |
| time over the response line (% of samples) | 43.02 | 41.32 | -4.0% | -2.742 to -0.6593 | GAIN |
| failed requests (%) | 23.71 | 25.31 | +6.8% | +1.064 to +2.146 | LOSS |
| HPA replicas, mean | 9.773 | 13.4 | +37.1% | +3.162 to +4.085 | power given |
| pods started | 3.293 | 6.927 | +110.4% | +2.843 to +4.426 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.815e-16 to +2.949e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.6 | +0.1% | -0.2585 to +0.5193 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.6 | +0.1% | -0.2585 to +0.5193 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.39 | 2.425 | +1.4% | +0.02739 to +0.04127 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.73 | 75.28 | +5.0% | +3.34 to +3.769 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | LOSS |
| organism behind its window (s) | 0.1415 | 0.1756 | +24.1% | +0.01406 to +0.05423 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
