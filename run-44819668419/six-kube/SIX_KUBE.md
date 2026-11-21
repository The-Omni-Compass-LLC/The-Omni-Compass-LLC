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
| response time (ms), 95th percentile | 1559 | 1243 | 1541 | 1714 | 1330 | 1140 | 1313 | 1062 | 1432 | 1421 | 1641 | 1559 | 1274 | 1151 |
| response time (ms), 99th percentile | 5045 | 4839 | 5562 | 5919 | 4436 | 3861 | 4385 | 4417 | 4717 | 4776 | 4872 | 4676 | 4762 | 4811 |
| time over the response line (% of samples) | 16.37 | 12.51 | 28.61 | 21.82 | 14.77 | 11.11 | 13.99 | 10.49 | 20.23 | 15.83 | 22.11 | 17.56 | 20.73 | 15.44 |
| failed requests (%) | 4.98 | 4.822 | 12.16 | 10.33 | 4.445 | 4.378 | 3.949 | 3.692 | 5.91 | 5.677 | 8.282 | 6.651 | 8.172 | 7.244 |
| HPA replicas, mean | 9.616 | 14.46 | 9.702 | 14.62 | 9.568 | 14.2 | 9.566 | 14.26 | 9.565 | 14.49 | 9.593 | 14.37 | 9.632 | 14.04 |
| pods started | 5.029 | 11.4 | 4.714 | 11.74 | 5.4 | 10.91 | 5.486 | 11.49 | 5.486 | 11.49 | 5.257 | 11.91 | 5.2 | 12.46 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 180.1 | 183.7 | 182.3 | 179.2 | 178.8 | 178.8 | 178.8 | 181.5 | 180.8 | 181.4 | 180.2 | 181 | 180.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 180.1 | 183.7 | 182.3 | 179.2 | 178.8 | 178.8 | 178.8 | 181.5 | 180.8 | 181.4 | 180.2 | 181 | 180.1 |
| CPU used with Omni's own (cores), mean | 1.938 | 1.988 | 2.258 | 2.288 | 1.855 | 1.891 | 1.84 | 1.879 | 2.042 | 2.084 | 2.033 | 2.068 | 2.009 | 2.043 |
| host CPU busy, the real machine under kind (%) | 57.93 | 59.58 | 66.92 | 68.4 | 55.75 | 57.08 | 55.12 | 56.59 | 60.8 | 62.5 | 60.65 | 62.11 | 60.15 | 61.68 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.08857 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1559 | 1243 | -20.3% | -559.2 to -72.8 | GAIN |
| response time (ms), 99th percentile | 5045 | 4839 | -4.1% | -660.8 to +249.5 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.37 | 12.51 | -23.6% | -4.94 to -2.776 | GAIN |
| failed requests (%) | 4.98 | 4.822 | -3.2% | -0.4843 to +0.1698 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.616 | 14.46 | +50.4% | +4.525 to +5.171 | power given |
| pods started | 5.029 | 11.4 | +126.7% | +5.837 to +6.905 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.966e-16 to +4.488e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 180.1 | +0.2% | -0.01917 to +0.7087 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 180.1 | +0.2% | -0.01917 to +0.7087 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.938 | 1.988 | +2.5% | +0.03455 to +0.06399 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.93 | 59.58 | +2.8% | +1.24 to +2.053 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.974e+05 to +7.996e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.416e-05 to -9.39e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1541 | 1714 | +11.2% | -38.23 to +383 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5562 | 5919 | +6.4% | -270.9 to +985.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 28.61 | 21.82 | -23.7% | -8.75 to -4.825 | GAIN |
| failed requests (%) | 12.16 | 10.33 | -15.0% | -3.014 to -0.6413 | GAIN |
| HPA replicas, mean | 9.702 | 14.62 | +50.7% | +4.718 to +5.118 | power given |
| pods started | 4.714 | 11.74 | +149.1% | +6.499 to +7.559 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.397e-16 to +5.412e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 182.3 | -0.7% | -1.74 to -0.905 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 182.3 | -0.7% | -1.74 to -0.905 | GAIN |
| CPU used with Omni's own (cores), mean | 2.258 | 2.288 | +1.3% | +0.01614 to +0.04398 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.92 | 68.4 | +2.2% | +1.164 to +1.793 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.619e+05 to +8.624e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.149e-05 to -8.144e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1330 | 1140 | -14.3% | -357.9 to -21.89 | GAIN |
| response time (ms), 99th percentile | 4436 | 3861 | -12.9% | -921.4 to -227.4 | GAIN |
| time over the response line (% of samples) | 14.77 | 11.11 | -24.8% | -4.824 to -2.496 | GAIN |
| failed requests (%) | 4.445 | 4.378 | -1.5% | -0.316 to +0.1816 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.568 | 14.2 | +48.4% | +4.154 to +5.116 | power given |
| pods started | 5.4 | 10.91 | +102.1% | +4.929 to +6.1 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.747e-16 to +2.194e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.2 | 178.8 | -0.2% | -0.9332 to +0.08783 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.2 | 178.8 | -0.2% | -0.9332 to +0.08783 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.855 | 1.891 | +1.9% | +0.02153 to +0.05082 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.75 | 57.08 | +2.4% | +0.9561 to +1.69 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1313 | 1062 | -19.1% | -540.1 to +38.55 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4385 | 4417 | +0.7% | -323.1 to +386.9 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 13.99 | 10.49 | -25.1% | -4.519 to -2.496 | GAIN |
| failed requests (%) | 3.949 | 3.692 | -6.5% | -0.5924 to +0.0786 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.566 | 14.26 | +49.1% | +4.264 to +5.122 | power given |
| pods started | 5.486 | 11.49 | +109.4% | +5.473 to +6.527 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.959e-16 to -1.46e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.8 | 178.8 | -0.0% | -0.4701 to +0.3227 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.8 | 178.8 | -0.0% | -0.4701 to +0.3227 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.84 | 1.879 | +2.2% | +0.02588 to +0.05328 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.12 | 56.59 | +2.7% | +1.101 to +1.838 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1432 | 1421 | -0.7% | -273.2 to +252.9 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4717 | 4776 | +1.3% | -390.9 to +509.7 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 20.23 | 15.83 | -21.8% | -5.651 to -3.156 | GAIN |
| failed requests (%) | 5.91 | 5.677 | -3.9% | -0.5191 to +0.05224 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.565 | 14.49 | +51.5% | +4.605 to +5.254 | power given |
| pods started | 5.486 | 11.49 | +109.4% | +5.388 to +6.612 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.004e-16 to +8.989e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.5 | 180.8 | -0.4% | -1.147 to -0.3549 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.5 | 180.8 | -0.4% | -1.147 to -0.3549 | GAIN |
| CPU used with Omni's own (cores), mean | 2.042 | 2.084 | +2.0% | +0.03282 to +0.05071 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.8 | 62.5 | +2.8% | +1.518 to +1.871 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1641 | 1559 | -5.0% | -278.6 to +116 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4872 | 4676 | -4.0% | -562.3 to +168.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 22.11 | 17.56 | -20.6% | -6.365 to -2.742 | GAIN |
| failed requests (%) | 8.282 | 6.651 | -19.7% | -2.831 to -0.4322 | GAIN |
| HPA replicas, mean | 9.593 | 14.37 | +49.8% | +4.538 to +5.009 | power given |
| pods started | 5.257 | 11.91 | +126.6% | +6.057 to +7.258 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.087e-15 to -2.945e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 180.2 | -0.7% | -1.674 to -0.8153 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 180.2 | -0.7% | -1.674 to -0.8153 | GAIN |
| CPU used with Omni's own (cores), mean | 2.033 | 2.068 | +1.7% | +0.02239 to +0.04692 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.65 | 62.11 | +2.4% | +1.155 to +1.781 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1274 | 1151 | -9.7% | -311 to +64.99 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4762 | 4811 | +1.0% | -373.8 to +471.8 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 20.73 | 15.44 | -25.5% | -7.079 to -3.49 | GAIN |
| failed requests (%) | 8.172 | 7.244 | -11.4% | -1.642 to -0.2148 | GAIN |
| HPA replicas, mean | 9.632 | 14.04 | +45.8% | +4.017 to +4.799 | power given |
| pods started | 5.2 | 12.46 | +139.6% | +6.66 to +7.854 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.785e-16 to -3.355e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180.1 | -0.5% | -1.351 to -0.4556 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180.1 | -0.5% | -1.351 to -0.4556 | GAIN |
| CPU used with Omni's own (cores), mean | 2.009 | 2.043 | +1.7% | +0.0216 to +0.04625 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.15 | 61.68 | +2.6% | +1.194 to +1.874 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.08857 | +0.0886 | +0.0747 to +0.1024 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
