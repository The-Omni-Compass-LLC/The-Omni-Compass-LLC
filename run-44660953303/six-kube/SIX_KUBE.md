# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on: native | The spine, the muscles every stack runs on: omni | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 833.5 | 928.4 | 871.1 | 964.5 | 1469 | 947.6 | 893.6 | 741.6 | 1123 | 1207 | 1864 | 1756 | 888.2 | 908.8 |
| response time (ms), 99th percentile | 3074 | 3797 | 3392 | 3667 | 4094 | 3896 | 3900 | 2895 | 3986 | 4605 | 4222 | 4311 | 3746 | 3951 |
| time over the response line (% of samples) | 10.11 | 7.569 | 15.55 | 11.68 | 13.23 | 9.611 | 11.58 | 8.155 | 17.67 | 14.09 | 27.08 | 22.7 | 13.3 | 10.32 |
| failed requests (%) | 2.51 | 2.375 | 6.111 | 5.741 | 3.257 | 3.581 | 3.761 | 3.625 | 4.574 | 4.895 | 10.52 | 10.21 | 4.532 | 4.265 |
| HPA replicas, mean | 9.513 | 14.19 | 9.589 | 14.04 | 9.544 | 14.53 | 9.473 | 13.38 | 9.531 | 14.33 | 9.553 | 14.1 | 9.572 | 14.24 |
| pods started | 6 | 12 | 5.4 | 12.4 | 5.7 | 12.4 | 6.1 | 10.9 | 5.8 | 11.4 | 5.2 | 11.9 | 5.7 | 12.9 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 177.3 | 178.2 | 179.3 | 178.8 | 178.6 | 179.2 | 177.1 | 177.7 | 180.7 | 180.1 | 180.4 | 180.2 | 179.3 | 178.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.3 | 178.2 | 179.3 | 178.8 | 178.6 | 179.2 | 177.1 | 177.7 | 180.7 | 180.1 | 180.4 | 180.2 | 179.3 | 178.5 |
| CPU used with Omni's own (cores), mean | 1.703 | 1.75 | 1.853 | 1.887 | 1.813 | 1.865 | 1.663 | 1.7 | 1.988 | 2.039 | 1.965 | 2.021 | 1.845 | 1.862 |
| host CPU busy, the real machine under kind (%) | 51.06 | 53.01 | 55.72 | 57.21 | 54.56 | 56.54 | 50.27 | 51.53 | 59.01 | 61.35 | 58.87 | 60.95 | 55.24 | 56.49 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.09 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 833.5 | 928.4 | +11.4% | -250.3 to +440.2 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3074 | 3797 | +23.5% | -198.2 to +1644 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 10.11 | 7.569 | -25.2% | -4.291 to -0.8001 | GAIN |
| failed requests (%) | 2.51 | 2.375 | -5.4% | -0.365 to +0.09367 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.513 | 14.19 | +49.2% | +3.928 to +5.426 | power given |
| pods started | 6 | 12 | +100.0% | +4.934 to +7.066 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.13e-15 to +2.421e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 177.3 | 178.2 | +0.5% | +0.5036 to +1.264 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.3 | 178.2 | +0.5% | +0.5036 to +1.264 | power given |
| CPU used with Omni's own (cores), mean | 1.703 | 1.75 | +2.7% | +0.0273 to +0.0663 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 51.06 | 53.01 | +3.8% | +1.485 to +2.412 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.98e+05 to +8.05e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.479e-05 to -9.397e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 871.1 | 964.5 | +10.7% | -237 to +423.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3392 | 3667 | +8.1% | -614 to +1163 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 15.55 | 11.68 | -24.9% | -7.255 to -0.4844 | GAIN |
| failed requests (%) | 6.111 | 5.741 | -6.1% | -1.779 to +1.038 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.589 | 14.04 | +46.5% | +3.512 to +5.398 | power given |
| pods started | 5.4 | 12.4 | +129.6% | +6.246 to +7.754 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.676e-15 to -2.778e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.3 | 178.8 | -0.3% | -1.201 to +0.1893 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.3 | 178.8 | -0.3% | -1.201 to +0.1893 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.853 | 1.887 | +1.8% | +3.219e-06 to +0.06681 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.72 | 57.21 | +2.7% | +0.5689 to +2.409 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.617e+05 to +8.628e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.152e-05 to -8.141e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1469 | 947.6 | -35.5% | -905.6 to -137.9 | GAIN |
| response time (ms), 99th percentile | 4094 | 3896 | -4.9% | -500.2 to +102.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 13.23 | 9.611 | -27.4% | -5.7 to -1.539 | GAIN |
| failed requests (%) | 3.257 | 3.581 | +10.0% | -0.3013 to +0.9509 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.544 | 14.53 | +52.2% | +4.622 to +5.349 | power given |
| pods started | 5.7 | 12.4 | +117.5% | +6.111 to +7.289 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.431e-15 to -1.676e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.6 | 179.2 | +0.3% | -0.05049 to +1.251 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.6 | 179.2 | +0.3% | -0.05049 to +1.251 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.813 | 1.865 | +2.9% | +0.03264 to +0.07137 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.56 | 56.54 | +3.6% | +1.682 to +2.268 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 893.6 | 741.6 | -17.0% | -584.5 to +280.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3900 | 2895 | -25.8% | -1669 to -341.9 | GAIN |
| time over the response line (% of samples) | 11.58 | 8.155 | -29.6% | -7.147 to +0.2923 | STEADY, inside the noise (cut) |
| failed requests (%) | 3.761 | 3.625 | -3.6% | -0.6846 to +0.4124 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.473 | 13.38 | +41.3% | +2.638 to +5.181 | power given |
| pods started | 6.1 | 10.9 | +78.7% | +3.642 to +5.958 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.499e-15 to -1.002e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 177.1 | 177.7 | +0.4% | +0.1025 to +1.152 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.1 | 177.7 | +0.4% | +0.1025 to +1.152 | power given |
| CPU used with Omni's own (cores), mean | 1.663 | 1.7 | +2.2% | +0.01366 to +0.05924 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 50.27 | 51.53 | +2.5% | +0.6296 to +1.874 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1123 | 1207 | +7.5% | -280.9 to +448.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3986 | 4605 | +15.5% | -647.2 to +1885 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 17.67 | 14.09 | -20.3% | -5.899 to -1.262 | GAIN |
| failed requests (%) | 4.574 | 4.895 | +7.0% | -0.1582 to +0.7988 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.531 | 14.33 | +50.4% | +3.952 to +5.651 | power given |
| pods started | 5.8 | 11.4 | +96.6% | +4.831 to +6.369 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.038e-15 to +3.277e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 180.1 | -0.3% | -1.504 to +0.3357 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 180.1 | -0.3% | -1.504 to +0.3357 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.988 | 2.039 | +2.6% | +0.0322 to +0.07128 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.01 | 61.35 | +4.0% | +1.675 to +3.002 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1864 | 1756 | -5.8% | -483.9 to +268.9 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4222 | 4311 | +2.1% | -347 to +525.9 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 27.08 | 22.7 | -16.2% | -7.53 to -1.223 | GAIN |
| failed requests (%) | 10.52 | 10.21 | -2.9% | -1.539 to +0.9226 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.553 | 14.1 | +47.6% | +3.866 to +5.234 | power given |
| pods started | 5.2 | 11.9 | +128.8% | +4.704 to +8.696 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.697e-16 to +6.697e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 180.2 | -0.1% | -0.9521 to +0.7134 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 180.2 | -0.1% | -0.9521 to +0.7134 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.965 | 2.021 | +2.8% | +0.04011 to +0.0713 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.87 | 60.95 | +3.5% | +1.573 to +2.598 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 888.2 | 908.8 | +2.3% | -437.3 to +478.4 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3746 | 3951 | +5.5% | -760.5 to +1170 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 13.3 | 10.32 | -22.4% | -5.837 to -0.1169 | GAIN |
| failed requests (%) | 4.532 | 4.265 | -5.9% | -1.85 to +1.316 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.572 | 14.24 | +48.8% | +4.171 to +5.17 | power given |
| pods started | 5.7 | 12.9 | +126.3% | +6.321 to +8.079 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.431e-15 to -1.676e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.3 | 178.5 | -0.5% | -1.636 to -0.04002 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.3 | 178.5 | -0.5% | -1.636 to -0.04002 | GAIN |
| CPU used with Omni's own (cores), mean | 1.845 | 1.862 | +1.0% | -0.008445 to +0.04435 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.24 | 56.49 | +2.3% | +0.2963 to +2.198 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.984e-09 | power given |
| organism behind its window (s) | 0 | 0.09 | +0.09 | +0.03722 to +0.1428 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
