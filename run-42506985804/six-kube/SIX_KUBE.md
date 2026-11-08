# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2869 | 3672 | 2082 | 3374 | 2550 | 3231 | 3212 | 3743 | 2086 | 2534 | 3317 | 3098 |
| response time (ms), 99th percentile | 5519 | 7062 | 3988 | 5768 | 5643 | 6348 | 5874 | 6280 | 4558 | 4993 | 6198 | 5990 |
| time over the response line (% of samples) | 49.89 | 46.62 | 46.34 | 42.32 | 39.19 | 36.82 | 39.47 | 37.96 | 25.73 | 22.06 | 55.65 | 51.32 |
| failed requests (%) | 32.32 | 32.01 | 24.2 | 25.71 | 24.78 | 24.11 | 23.69 | 22.29 | 9.496 | 9.511 | 34.59 | 35.1 |
| HPA replicas, mean | 9.658 | 14.09 | 9.692 | 12.59 | 9.636 | 14.2 | 9.601 | 14.59 | 9.58 | 13.91 | 9.726 | 11.54 |
| pods started | 4.85 | 10.2 | 4.55 | 9.35 | 4.9 | 11.15 | 5.6 | 11.25 | 6 | 12.25 | 4.1 | 8.65 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.8 | 185.4 | 184.5 | 184.6 | 184.3 | 184.4 | 184.4 | 183.7 | 182.6 | 182.8 | 185.6 | 185.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.8 | 185.4 | 184.5 | 184.6 | 184.3 | 184.4 | 184.4 | 183.7 | 182.6 | 182.8 | 185.6 | 185.5 |
| CPU used with Omni's own (cores), mean | 2.461 | 2.508 | 2.421 | 2.465 | 2.379 | 2.428 | 2.368 | 2.416 | 2.205 | 2.254 | 2.531 | 2.567 |
| host CPU busy, the real machine under kind (%) | 72.62 | 74.33 | 71.1 | 73.25 | 70.23 | 72.21 | 69.7 | 71.81 | 64.5 | 66.81 | 75.11 | 77.52 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 |
| organism behind its window (s) | 0 | 0 | 0.015 | 0.02 | 0 | 0 | 0 | 0.005 | 0 | 0.005 | 0.095 | 0.21 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2869 | 3672 | +28.0% | -73.74 to +1680 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5519 | 7062 | +28.0% | +664.6 to +2422 | LOSS |
| time over the response line (% of samples) | 49.89 | 46.62 | -6.6% | -4.842 to -1.701 | GAIN |
| failed requests (%) | 32.32 | 32.01 | -0.9% | -1.939 to +1.329 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.658 | 14.09 | +45.8% | +4.023 to +4.832 | power given |
| pods started | 4.85 | 10.2 | +110.3% | +4.557 to +6.143 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.238e-16 to +1.797e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.8 | 185.4 | +0.3% | -0.2413 to +1.411 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.8 | 185.4 | +0.3% | -0.2413 to +1.411 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.461 | 2.508 | +1.9% | +0.0329 to +0.06105 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.62 | 74.33 | +2.4% | +1.329 to +2.092 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2082 | 3374 | +62.1% | +551.8 to +2034 | LOSS |
| response time (ms), 99th percentile | 3988 | 5768 | +44.6% | +613.4 to +2948 | LOSS |
| time over the response line (% of samples) | 46.34 | 42.32 | -8.7% | -6.012 to -2.032 | GAIN |
| failed requests (%) | 24.2 | 25.71 | +6.2% | +0.3955 to +2.615 | LOSS |
| HPA replicas, mean | 9.692 | 12.59 | +29.9% | +2.042 to +3.762 | power given |
| pods started | 4.55 | 9.35 | +105.5% | +3.809 to +5.791 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.811e-16 to -7.083e-18 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.6 | +0.1% | -0.5693 to +0.8154 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.6 | +0.1% | -0.5693 to +0.8154 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.421 | 2.465 | +1.8% | +0.03597 to +0.05245 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.1 | 73.25 | +3.0% | +1.831 to +2.463 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.015 | 0.02 | +33.3% | -0.01889 to +0.02889 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2550 | 3231 | +26.7% | -211.9 to +1573 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5643 | 6348 | +12.5% | -259.4 to +1669 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 39.19 | 36.82 | -6.0% | -3.824 to -0.905 | GAIN |
| failed requests (%) | 24.78 | 24.11 | -2.7% | -2.268 to +0.9263 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.636 | 14.2 | +47.4% | +4.223 to +4.903 | power given |
| pods started | 4.9 | 11.15 | +127.6% | +5.493 to +7.007 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.897e-16 to +4.345e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.4 | +0.0% | -0.6895 to +0.8403 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.4 | +0.0% | -0.6895 to +0.8403 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.379 | 2.428 | +2.1% | +0.04001 to +0.0576 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.23 | 72.21 | +2.8% | +1.735 to +2.217 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3212 | 3743 | +16.5% | -127.7 to +1191 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5874 | 6280 | +6.9% | -234.9 to +1046 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 39.47 | 37.96 | -3.8% | -2.723 to -0.2975 | GAIN |
| failed requests (%) | 23.69 | 22.29 | -5.9% | -2.884 to +0.07914 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.601 | 14.59 | +51.9% | +4.724 to +5.247 | power given |
| pods started | 5.6 | 11.25 | +100.9% | +4.902 to +6.398 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.163e-15 to -8.059e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 183.7 | -0.4% | -1.265 to -0.2024 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 183.7 | -0.4% | -1.265 to -0.2024 | GAIN |
| CPU used with Omni's own (cores), mean | 2.368 | 2.416 | +2.0% | +0.03307 to +0.06153 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.7 | 71.81 | +3.0% | +1.635 to +2.585 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0 | 0.005 | +0.005 | -0.005465 to +0.01546 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2086 | 2534 | +21.5% | -301.3 to +1198 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4558 | 4993 | +9.5% | -200.6 to +1070 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 25.73 | 22.06 | -14.3% | -5.204 to -2.15 | GAIN |
| failed requests (%) | 9.496 | 9.511 | +0.2% | -1.05 to +1.079 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.58 | 13.91 | +45.2% | +3.729 to +4.928 | power given |
| pods started | 6 | 12.25 | +104.2% | +5.178 to +7.322 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.019e-15 to +4.203e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.6 | 182.8 | +0.1% | -0.5764 to +1.016 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.6 | 182.8 | +0.1% | -0.5764 to +1.016 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.205 | 2.254 | +2.2% | +0.03082 to +0.06655 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.5 | 66.81 | +3.6% | +1.723 to +2.907 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0 | 0.005 | +0.005 | -0.005465 to +0.01546 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3317 | 3098 | -6.6% | -1011 to +571.9 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6198 | 5990 | -3.4% | -1108 to +690.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 55.65 | 51.32 | -7.8% | -6.241 to -2.42 | GAIN |
| failed requests (%) | 34.59 | 35.1 | +1.5% | -1.89 to +2.907 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.726 | 11.54 | +18.7% | +0.8512 to +2.781 | power given |
| pods started | 4.1 | 8.65 | +111.0% | +3.482 to +5.618 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.195e-15 to -4.796e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.6 | 185.5 | -0.0% | -0.6852 to +0.5101 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.6 | 185.5 | -0.0% | -0.6852 to +0.5101 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.531 | 2.567 | +1.5% | +0.0219 to +0.0515 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.11 | 77.52 | +3.2% | +1.898 to +2.935 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.095 | 0.21 | +121.1% | +0.09785 to +0.1321 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
