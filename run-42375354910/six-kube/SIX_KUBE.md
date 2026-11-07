# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3398 | 4419 | 3467 | 3600 | 2674 | 2934 | 2039 | 3682 | 2789 | 3262 | 2475 | 4109 |
| response time (ms), 99th percentile | 6078 | 7484 | 6331 | 6571 | 4673 | 5051 | 4560 | 5596 | 5061 | 5799 | 4500 | 5955 |
| time over the response line (% of samples) | 49.22 | 46.2 | 42.49 | 38.94 | 31.13 | 31.03 | 36.34 | 34.64 | 44.34 | 40.53 | 42.52 | 42.94 |
| failed requests (%) | 30.96 | 31.1 | 26.43 | 26.14 | 20 | 21.33 | 20.08 | 21.78 | 27.6 | 25.5 | 21.28 | 24.4 |
| HPA replicas, mean | 9.657 | 14.29 | 9.605 | 14.13 | 9.589 | 14.27 | 9.635 | 13.34 | 9.66 | 12.37 | 9.692 | 13.05 |
| pods started | 4.85 | 10.25 | 5.4 | 11.1 | 5.211 | 11.35 | 5.2 | 10.9 | 4.9 | 9.95 | 4.55 | 9.2 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 185.2 | 185.4 | 184.4 | 184.1 | 182.3 | 182.6 | 183.2 | 183.8 | 184 | 183.9 | 184.5 | 184.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.2 | 185.4 | 184.4 | 184.1 | 182.3 | 182.6 | 183.2 | 183.8 | 184 | 183.9 | 184.5 | 184.5 |
| CPU used with Omni's own (cores), mean | 2.502 | 2.55 | 2.408 | 2.445 | 2.194 | 2.251 | 2.275 | 2.33 | 2.357 | 2.394 | 2.398 | 2.456 |
| host CPU busy, the real machine under kind (%) | 73.44 | 75.45 | 70.89 | 72.49 | 65.02 | 67.41 | 66.72 | 69.04 | 69.73 | 72.25 | 71.51 | 75.78 |
| organism work | 2.148e+11 | 2.148e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0.005 | 0 | 0.005 | 0.01053 | 0.01 | 0.005 | 0.005 | 0.1 | 0.225 | 0.17 | 0.175 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3398 | 4419 | +30.0% | -125.3 to +2166 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6078 | 7484 | +23.1% | +540.4 to +2271 | LOSS |
| time over the response line (% of samples) | 49.22 | 46.2 | -6.2% | -4.579 to -1.478 | GAIN |
| failed requests (%) | 30.96 | 31.1 | +0.5% | -1.044 to +1.323 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.657 | 14.29 | +47.9% | +4.231 to +5.028 | power given |
| pods started | 4.85 | 10.25 | +111.3% | +4.767 to +6.033 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.111e-15 to +4.559e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.2 | 185.4 | +0.1% | -0.7174 to +1.063 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.2 | 185.4 | +0.1% | -0.7174 to +1.063 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.502 | 2.55 | +1.9% | +0.03676 to +0.05781 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.44 | 75.45 | +2.7% | +1.788 to +2.219 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0.005 | +0.005 | -0.005465 to +0.01546 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3467 | 3600 | +3.9% | -1260 to +1527 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6331 | 6571 | +3.8% | -661.5 to +1141 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 42.49 | 38.94 | -8.4% | -5.343 to -1.759 | GAIN |
| failed requests (%) | 26.43 | 26.14 | -1.1% | -2.702 to +2.133 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.605 | 14.13 | +47.2% | +4.142 to +4.919 | power given |
| pods started | 5.4 | 11.1 | +105.6% | +4.97 to +6.43 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.405e-16 to +4.74e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.1 | -0.2% | -1.059 to +0.4995 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.1 | -0.2% | -1.059 to +0.4995 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.408 | 2.445 | +1.5% | +0.02208 to +0.05193 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.89 | 72.49 | +2.2% | +1.101 to +2.086 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0 | 0.005 | +0.005 | -0.005465 to +0.01546 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

19 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2674 | 2894 | +8.2% | -715 to +1155 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4673 | 4909 | +5.1% | -356.4 to +829 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 31.13 | 29.83 | -4.2% | -2.447 to -0.153 | GAIN |
| failed requests (%) | 20 | 20.26 | +1.3% | -1.176 to +1.693 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.589 | 14.23 | +48.4% | +4.326 to +4.955 | power given |
| pods started | 5.211 | 11.32 | +117.2% | +5.103 to +7.107 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.79e-16 to +5.53e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 182.4 | +0.1% | -0.5321 to +0.7371 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 182.4 | +0.1% | -0.5321 to +0.7371 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.194 | 2.231 | +1.7% | +0.01425 to +0.06027 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.02 | 66.86 | +2.8% | +1.261 to +2.41 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.01053 | 0.01053 | +0.0% | -0.02272 to +0.02272 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2039 | 3682 | +80.6% | +525.3 to +2761 | LOSS |
| response time (ms), 99th percentile | 4560 | 5596 | +22.7% | +147.2 to +1924 | LOSS |
| time over the response line (% of samples) | 36.34 | 34.64 | -4.7% | -3.352 to -0.0423 | GAIN |
| failed requests (%) | 20.08 | 21.78 | +8.5% | +0.5078 to +2.907 | LOSS |
| HPA replicas, mean | 9.635 | 13.34 | +38.5% | +2.942 to +4.47 | power given |
| pods started | 5.2 | 10.9 | +109.6% | +5.036 to +6.364 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.428e-16 to +3.763e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.2 | 183.8 | +0.3% | -0.1402 to +1.292 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.2 | 183.8 | +0.3% | -0.1402 to +1.292 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.275 | 2.33 | +2.4% | +0.04416 to +0.06521 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.72 | 69.04 | +3.5% | +1.99 to +2.633 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.005 | 0.005 | +0.0% | -0.01518 to +0.01518 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2789 | 3262 | +17.0% | -575.7 to +1521 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5061 | 5799 | +14.6% | -303.8 to +1779 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 44.34 | 40.53 | -8.6% | -5.58 to -2.045 | GAIN |
| failed requests (%) | 27.6 | 25.5 | -7.6% | -3.879 to -0.3132 | GAIN |
| HPA replicas, mean | 9.66 | 12.37 | +28.0% | +1.8 to +3.611 | power given |
| pods started | 4.9 | 9.95 | +103.1% | +4.415 to +5.685 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.55e-16 to +7.103e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 183.9 | -0.1% | -0.7687 to +0.5579 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 183.9 | -0.1% | -0.7687 to +0.5579 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.357 | 2.394 | +1.6% | +0.03002 to +0.0435 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.73 | 72.25 | +3.6% | +2.344 to +2.693 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1 | 0.225 | +125.0% | +0.07976 to +0.1702 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2475 | 4109 | +66.1% | +721.5 to +2548 | LOSS |
| response time (ms), 99th percentile | 4500 | 5955 | +32.3% | +246.8 to +2663 | LOSS |
| time over the response line (% of samples) | 42.52 | 42.94 | +1.0% | -2.233 to +3.059 | STEADY, inside the noise (up) |
| failed requests (%) | 21.28 | 24.4 | +14.6% | +1.412 to +4.822 | LOSS |
| HPA replicas, mean | 9.692 | 13.05 | +34.7% | +2.371 to +4.347 | power given |
| pods started | 4.55 | 9.2 | +102.2% | +3.471 to +5.829 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.03e-16 to +5.918e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.5 | -0.0% | -0.5263 to +0.4097 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.5 | -0.0% | -0.5263 to +0.4097 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.398 | 2.456 | +2.4% | +0.04598 to +0.07145 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.51 | 75.78 | +6.0% | +3.923 to +4.622 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.17 | 0.175 | +2.9% | -0.02712 to +0.03712 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
