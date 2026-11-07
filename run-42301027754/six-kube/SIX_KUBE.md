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
| response time (ms), 95th percentile | 1101 | 899.4 | 1366 | 1288 | 1597 | 1224 | 1938 | 1663 | 1804 | 1439 | 910 | 880 |
| response time (ms), 99th percentile | 3872 | 3475 | 4515 | 3870 | 4690 | 4760 | 5989 | 5420 | 4366 | 4243 | 3271 | 3291 |
| time over the response line (% of samples) | 13.29 | 9.313 | 21.05 | 16.25 | 15.35 | 11.36 | 20.96 | 16.9 | 22.76 | 18.41 | 13.94 | 11.87 |
| failed requests (%) | 4.762 | 3.896 | 8.79 | 7.8 | 4.133 | 3.79 | 7.104 | 6.789 | 8.853 | 8.477 | 5.151 | 5.304 |
| HPA replicas, mean | 9.507 | 13.49 | 9.615 | 13.76 | 9.57 | 14.26 | 9.654 | 14.65 | 9.573 | 14 | 9.54 | 14.11 |
| pods started | 5.75 | 12.12 | 5.25 | 12.25 | 5.375 | 11.75 | 4.5 | 10.88 | 5.125 | 12.25 | 6 | 12.62 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 177.5 | 177.7 | 181.1 | 180.1 | 179.5 | 179.6 | 180.8 | 181.7 | 180.4 | 179.4 | 178.7 | 177.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.5 | 177.7 | 181.1 | 180.1 | 179.5 | 179.6 | 180.8 | 181.7 | 180.4 | 179.4 | 178.7 | 177.7 |
| CPU used with Omni's own (cores), mean | 1.7 | 1.758 | 2.01 | 2.042 | 1.872 | 1.914 | 2.079 | 2.11 | 1.95 | 1.991 | 1.796 | 1.828 |
| host CPU busy, the real machine under kind (%) | 51.14 | 53.12 | 60.07 | 61.11 | 55.85 | 57.53 | 61.49 | 62.97 | 58.42 | 59.87 | 53.75 | 55.33 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0.275 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0875 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1101 | 899.4 | -18.3% | -297.4 to -105.1 | GAIN |
| response time (ms), 99th percentile | 3872 | 3475 | -10.3% | -875.2 to +80.05 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 13.29 | 9.313 | -29.9% | -8.091 to +0.142 | STEADY, inside the noise (cut) |
| failed requests (%) | 4.762 | 3.896 | -18.2% | -1.918 to +0.1859 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.507 | 13.49 | +41.8% | +2.857 to +5.099 | power given |
| pods started | 5.75 | 12.12 | +110.9% | +4.831 to +7.919 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.803e-16 to +4.362e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 177.5 | 177.7 | +0.1% | -0.8534 to +1.282 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.5 | 177.7 | +0.1% | -0.8534 to +1.282 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.7 | 1.758 | +3.4% | +0.03239 to +0.08296 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 51.14 | 53.12 | +3.9% | +0.7536 to +3.205 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.978e+05 to +8.004e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.425e-05 to -9.395e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1366 | 1288 | -5.7% | -326.6 to +170.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4515 | 3870 | -14.3% | -1462 to +171.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 21.05 | 16.25 | -22.8% | -9.716 to +0.1193 | STEADY, inside the noise (cut) |
| failed requests (%) | 8.79 | 7.8 | -11.3% | -3.628 to +1.65 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.615 | 13.76 | +43.1% | +3.004 to +5.292 | power given |
| pods started | 5.25 | 12.25 | +133.3% | +5.817 to +8.183 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.037e-15 to +8.146e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 180.1 | -0.6% | -1.978 to -0.04939 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 180.1 | -0.6% | -1.978 to -0.04939 | GAIN |
| CPU used with Omni's own (cores), mean | 2.01 | 2.042 | +1.6% | -0.004731 to +0.06737 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.07 | 61.11 | +1.7% | +0.02546 to +2.067 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.616e+05 to +8.631e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.155e-05 to -8.141e-05 | power given |
| organism behind its window (s) | 0 | 0.275 | +0.275 | -0.3754 to +0.9254 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1597 | 1224 | -23.4% | -852.5 to +105.8 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4690 | 4760 | +1.5% | -393.1 to +533.8 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 15.35 | 11.36 | -26.0% | -6.616 to -1.367 | GAIN |
| failed requests (%) | 4.133 | 3.79 | -8.3% | -1.291 to +0.6056 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.57 | 14.26 | +49.0% | +3.993 to +5.378 | power given |
| pods started | 5.375 | 11.75 | +118.6% | +5.116 to +7.634 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.907e-17 to +1.613e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.5 | 179.6 | +0.0% | -1.12 to +1.287 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.5 | 179.6 | +0.0% | -1.12 to +1.287 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.872 | 1.914 | +2.2% | +0.02855 to +0.05437 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.85 | 57.53 | +3.0% | +1.139 to +2.216 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 4

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1938 | 1663 | -14.2% | -1475 to +926.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5989 | 5420 | -9.5% | -1350 to +212.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 20.96 | 16.9 | -19.4% | -8.239 to +0.1171 | STEADY, inside the noise (cut) |
| failed requests (%) | 7.104 | 6.789 | -4.4% | -1.454 to +0.8241 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.654 | 14.65 | +51.8% | +4.427 to +5.571 | power given |
| pods started | 4.5 | 10.88 | +141.7% | +4.099 to +8.651 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.416e-15 to +5.283e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 181.7 | +0.5% | +0.02361 to +1.773 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 181.7 | +0.5% | +0.02361 to +1.773 | power given |
| CPU used with Omni's own (cores), mean | 2.079 | 2.11 | +1.5% | -0.0082 to +0.07024 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.49 | 62.97 | +2.4% | +0.8149 to +2.139 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1804 | 1439 | -20.2% | -788.3 to +58.22 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4366 | 4243 | -2.8% | -1422 to +1176 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 22.76 | 18.41 | -19.1% | -7.767 to -0.9432 | GAIN |
| failed requests (%) | 8.853 | 8.477 | -4.2% | -1.66 to +0.9078 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.573 | 14 | +46.2% | +3.332 to +5.517 | power given |
| pods started | 5.125 | 12.25 | +139.0% | +5.427 to +8.823 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.467e-16 to +9.908e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 179.4 | -0.6% | -1.998 to -0.06671 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 179.4 | -0.6% | -1.998 to -0.06671 | GAIN |
| CPU used with Omni's own (cores), mean | 1.95 | 1.991 | +2.1% | +0.01959 to +0.06267 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.42 | 59.87 | +2.5% | +0.7768 to +2.118 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 910 | 880 | -3.3% | -224.4 to +164.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3271 | 3291 | +0.6% | -1064 to +1104 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 13.94 | 11.87 | -14.8% | -4.508 to +0.3703 | STEADY, inside the noise (cut) |
| failed requests (%) | 5.151 | 5.304 | +3.0% | -0.4924 to +0.7987 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.54 | 14.11 | +48.0% | +3.956 to +5.193 | power given |
| pods started | 6 | 12.62 | +110.4% | +5.536 to +7.714 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.013e-15 to +3.473e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.7 | 177.7 | -0.6% | -1.896 to -0.1215 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.7 | 177.7 | -0.6% | -1.896 to -0.1215 | GAIN |
| CPU used with Omni's own (cores), mean | 1.796 | 1.828 | +1.8% | -0.003129 to +0.06649 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 53.75 | 55.33 | +2.9% | +0.5252 to +2.638 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.984e-09 | power given |
| organism behind its window (s) | 0 | 0.0875 | +0.0875 | +0.05794 to +0.1171 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Distribution / Specialized

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
