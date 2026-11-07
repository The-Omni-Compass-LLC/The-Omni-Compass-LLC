# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on: native | The spine, the muscles every stack runs on: omni | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1560 | 1359 | 1250 | 1420 | 1930 | 1780 | 1101 | 930.5 | 1644 | 1444 | 1209 | 1367 |
| response time (ms), 99th percentile | 4897 | 4755 | 4514 | 4741 | 6043 | 5693 | 3912 | 3581 | 4493 | 3978 | 4344 | 4713 |
| time over the response line (% of samples) | 15 | 11.56 | 22.84 | 17.06 | 21.65 | 16.53 | 12.09 | 8.858 | 23.16 | 18.13 | 21.94 | 16.61 |
| failed requests (%) | 4.374 | 4.078 | 9.676 | 8.08 | 7.423 | 6.913 | 3.43 | 3.257 | 8.647 | 7.386 | 9.019 | 7.651 |
| HPA replicas, mean | 9.582 | 14.22 | 9.631 | 14.22 | 9.644 | 14.39 | 9.532 | 14.02 | 9.581 | 14.15 | 9.626 | 14.52 |
| pods started | 5.341 | 11.22 | 5.366 | 11.61 | 4.707 | 11 | 5.707 | 11.63 | 5.073 | 11.68 | 5.22 | 11.85 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.2 | 179.7 | 181.4 | 180.7 | 180.9 | 181.4 | 177.9 | 178.2 | 180.9 | 180 | 181.3 | 180.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.2 | 179.7 | 181.4 | 180.7 | 180.9 | 181.4 | 177.9 | 178.2 | 180.9 | 180 | 181.3 | 180.5 |
| CPU used with Omni's own (cores), mean | 1.883 | 1.925 | 2.065 | 2.098 | 2.067 | 2.113 | 1.744 | 1.786 | 1.997 | 2.034 | 2.037 | 2.073 |
| host CPU busy, the real machine under kind (%) | 56.19 | 57.74 | 61.36 | 62.73 | 61.37 | 62.94 | 52.26 | 53.96 | 59.66 | 60.91 | 60.78 | 62.32 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.08049 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1560 | 1359 | -12.9% | -443.3 to +42.18 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4897 | 4755 | -2.9% | -469.5 to +184.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 15 | 11.56 | -22.9% | -4.328 to -2.557 | GAIN |
| failed requests (%) | 4.374 | 4.078 | -6.8% | -0.5525 to -0.04044 | GAIN |
| HPA replicas, mean | 9.582 | 14.22 | +48.4% | +4.27 to +5.01 | power given |
| pods started | 5.341 | 11.22 | +110.0% | +5.431 to +6.326 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.548e-16 to +9.155e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.2 | 179.7 | +0.3% | +0.1371 to +0.8933 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.2 | 179.7 | +0.3% | +0.1371 to +0.8933 | power given |
| CPU used with Omni's own (cores), mean | 1.883 | 1.925 | +2.2% | +0.03102 to +0.05261 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.19 | 57.74 | +2.8% | +1.316 to +1.786 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.978e+05 to +8.006e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.427e-05 to -9.394e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1250 | 1420 | +13.5% | -52.25 to +391.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4514 | 4741 | +5.0% | -260.9 to +716.6 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 22.84 | 17.06 | -25.3% | -7.569 to -3.986 | GAIN |
| failed requests (%) | 9.676 | 8.08 | -16.5% | -2.357 to -0.8362 | GAIN |
| HPA replicas, mean | 9.631 | 14.22 | +47.6% | +4.307 to +4.861 | power given |
| pods started | 5.366 | 11.61 | +116.4% | +5.822 to +6.666 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.324e-16 to +2.292e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 180.7 | -0.4% | -1.109 to -0.2624 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 180.7 | -0.4% | -1.109 to -0.2624 | GAIN |
| CPU used with Omni's own (cores), mean | 2.065 | 2.098 | +1.6% | +0.02136 to +0.04563 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.36 | 62.73 | +2.2% | +1.077 to +1.649 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.62e+05 to +8.625e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.149e-05 to -8.145e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1930 | 1780 | -7.7% | -433.1 to +134.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6043 | 5693 | -5.8% | -744.6 to +45.58 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 21.65 | 16.53 | -23.6% | -6.2 to -4.028 | GAIN |
| failed requests (%) | 7.423 | 6.913 | -6.9% | -0.9391 to -0.08082 | GAIN |
| HPA replicas, mean | 9.644 | 14.39 | +49.2% | +4.405 to +5.094 | power given |
| pods started | 4.707 | 11 | +133.7% | +5.839 to +6.746 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.331e-16 to +6.986e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 181.4 | +0.3% | -0.05209 to +0.9806 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 181.4 | +0.3% | -0.05209 to +0.9806 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.067 | 2.113 | +2.2% | +0.03139 to +0.05915 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.37 | 62.94 | +2.6% | +1.219 to +1.914 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1101 | 930.5 | -15.5% | -364.9 to +23.58 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3912 | 3581 | -8.5% | -634.2 to -28.99 | GAIN |
| time over the response line (% of samples) | 12.09 | 8.858 | -26.7% | -4.314 to -2.146 | GAIN |
| failed requests (%) | 3.43 | 3.257 | -5.0% | -0.4763 to +0.1305 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.532 | 14.02 | +47.1% | +4.072 to +4.908 | power given |
| pods started | 5.707 | 11.63 | +103.8% | +5.462 to +6.392 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.07e-16 to +3.503e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 177.9 | 178.2 | +0.2% | -0.09313 to +0.732 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.9 | 178.2 | +0.2% | -0.09313 to +0.732 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.744 | 1.786 | +2.4% | +0.03015 to +0.05405 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 52.26 | 53.96 | +3.3% | +1.432 to +1.977 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 7 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 0

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1644 | 1444 | -12.2% | -320.7 to -79.12 | GAIN |
| response time (ms), 99th percentile | 4493 | 3978 | -11.5% | -934.9 to -94.46 | GAIN |
| time over the response line (% of samples) | 23.16 | 18.13 | -21.7% | -6.791 to -3.28 | GAIN |
| failed requests (%) | 8.647 | 7.386 | -14.6% | -2.192 to -0.3297 | GAIN |
| HPA replicas, mean | 9.581 | 14.15 | +47.7% | +4.244 to +4.902 | power given |
| pods started | 5.073 | 11.68 | +130.3% | +5.971 to +7.248 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.086e-16 to +4.552e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 180 | -0.5% | -1.28 to -0.4302 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 180 | -0.5% | -1.28 to -0.4302 | GAIN |
| CPU used with Omni's own (cores), mean | 1.997 | 2.034 | +1.8% | +0.0207 to +0.05214 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.66 | 60.91 | +2.1% | +0.7699 to +1.721 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1209 | 1367 | +13.0% | -69.49 to +384.4 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4344 | 4713 | +8.5% | -100.8 to +838.9 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 21.94 | 16.61 | -24.3% | -6.978 to -3.67 | GAIN |
| failed requests (%) | 9.019 | 7.651 | -15.2% | -2.281 to -0.455 | GAIN |
| HPA replicas, mean | 9.626 | 14.52 | +50.9% | +4.693 to +5.1 | power given |
| pods started | 5.22 | 11.85 | +127.1% | +6.084 to +7.184 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.266e-16 to +2.007e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.3 | 180.5 | -0.5% | -1.231 to -0.4373 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.3 | 180.5 | -0.5% | -1.231 to -0.4373 | GAIN |
| CPU used with Omni's own (cores), mean | 2.037 | 2.073 | +1.7% | +0.02587 to +0.04508 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.78 | 62.32 | +2.5% | +1.28 to +1.8 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.08049 | +0.0805 | +0.06599 to +0.09499 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Distribution / Specialized

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
