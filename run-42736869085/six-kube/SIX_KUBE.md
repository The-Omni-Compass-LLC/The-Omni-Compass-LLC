# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on: native | The spine, the muscles every stack runs on: omni | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1373 | 1361 | 1226 | 1304 | 1400 | 1269 | 1159 | 1116 | 1448 | 1412 | 1368 | 1319 |
| response time (ms), 99th percentile | 5034 | 4846 | 4003 | 4465 | 4618 | 4454 | 3561 | 3660 | 4039 | 4221 | 4155 | 4444 |
| time over the response line (% of samples) | 15.45 | 11.55 | 21.32 | 16.41 | 15.93 | 11.92 | 16.85 | 12.63 | 20.44 | 16.43 | 24.05 | 18.74 |
| failed requests (%) | 4.31 | 3.957 | 8.738 | 7.761 | 4.811 | 4.492 | 4.78 | 4.709 | 7.527 | 6.734 | 10.43 | 9.121 |
| HPA replicas, mean | 9.588 | 14.37 | 9.619 | 14.34 | 9.563 | 14.1 | 9.516 | 14.02 | 9.534 | 14.04 | 9.654 | 13.89 |
| pods started | 5.22 | 11.83 | 5.341 | 12.39 | 5.488 | 11.17 | 5.659 | 11.78 | 5.707 | 12.07 | 4.854 | 11.66 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.2 | 179.8 | 180.8 | 180.3 | 179.2 | 179.6 | 179.4 | 179.2 | 180.1 | 179.6 | 181.8 | 181.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.2 | 179.8 | 180.8 | 180.3 | 179.2 | 179.6 | 179.4 | 179.2 | 180.1 | 179.6 | 181.8 | 181.2 |
| CPU used with Omni's own (cores), mean | 1.896 | 1.94 | 2.001 | 2.042 | 1.883 | 1.931 | 1.878 | 1.929 | 1.934 | 1.974 | 2.087 | 2.129 |
| host CPU busy, the real machine under kind (%) | 56.49 | 57.91 | 59.49 | 61.09 | 56.11 | 57.72 | 56.09 | 57.98 | 57.75 | 59.22 | 62.36 | 63.97 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.09024 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1373 | 1361 | -0.9% | -266.4 to +242.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5034 | 4846 | -3.7% | -518.5 to +141.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 15.45 | 11.55 | -25.2% | -4.875 to -2.916 | GAIN |
| failed requests (%) | 4.31 | 3.957 | -8.2% | -0.7134 to +0.007539 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.588 | 14.37 | +49.9% | +4.504 to +5.063 | power given |
| pods started | 5.22 | 11.83 | +126.6% | +6.127 to +7.093 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.01e-16 to -1.821e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.2 | 179.8 | +0.4% | +0.2979 to +0.9768 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.2 | 179.8 | +0.4% | +0.2979 to +0.9768 | power given |
| CPU used with Omni's own (cores), mean | 1.896 | 1.94 | +2.3% | +0.03424 to +0.05432 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.49 | 57.91 | +2.5% | +1.147 to +1.689 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.981e+05 to +8.002e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.423e-05 to -9.398e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1226 | 1304 | +6.4% | -87.38 to +243.4 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4003 | 4465 | +11.6% | -65.92 to +990.8 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 21.32 | 16.41 | -23.1% | -6.318 to -3.514 | GAIN |
| failed requests (%) | 8.738 | 7.761 | -11.2% | -1.578 to -0.3765 | GAIN |
| HPA replicas, mean | 9.619 | 14.34 | +49.1% | +4.444 to +5.002 | power given |
| pods started | 5.341 | 12.39 | +132.0% | +6.555 to +7.543 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.22e-16 to +1.154e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 180.3 | -0.2% | -0.8764 to -0.0187 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 180.3 | -0.2% | -0.8764 to -0.0187 | GAIN |
| CPU used with Omni's own (cores), mean | 2.001 | 2.042 | +2.0% | +0.02839 to +0.05189 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.49 | 61.09 | +2.7% | +1.221 to +1.994 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.622e+05 to +8.626e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.15e-05 to -8.147e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1400 | 1269 | -9.4% | -335.8 to +72.73 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4618 | 4454 | -3.6% | -508.1 to +178.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 15.93 | 11.92 | -25.2% | -5.091 to -2.927 | GAIN |
| failed requests (%) | 4.811 | 4.492 | -6.6% | -0.6355 to -0.002513 | GAIN |
| HPA replicas, mean | 9.563 | 14.1 | +47.5% | +4.11 to +4.966 | power given |
| pods started | 5.488 | 11.17 | +103.6% | +5.095 to +6.271 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.103e-16 to +4.536e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.2 | 179.6 | +0.2% | +0.03171 to +0.797 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.2 | 179.6 | +0.2% | +0.03171 to +0.797 | power given |
| CPU used with Omni's own (cores), mean | 1.883 | 1.931 | +2.5% | +0.03895 to +0.05593 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.11 | 57.72 | +2.9% | +1.421 to +1.799 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1159 | 1116 | -3.7% | -200.6 to +114.7 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3561 | 3660 | +2.8% | -229.9 to +428.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 16.85 | 12.63 | -25.0% | -5.759 to -2.68 | GAIN |
| failed requests (%) | 4.78 | 4.709 | -1.5% | -0.3677 to +0.2252 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.516 | 14.02 | +47.4% | +4.129 to +4.888 | power given |
| pods started | 5.659 | 11.78 | +108.2% | +5.658 to +6.586 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.854e-16 to +2.388e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.4 | 179.2 | -0.1% | -0.6492 to +0.223 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.4 | 179.2 | -0.1% | -0.6492 to +0.223 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.878 | 1.929 | +2.7% | +0.0388 to +0.06244 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.09 | 57.98 | +3.4% | +1.567 to +2.219 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1448 | 1412 | -2.5% | -234.3 to +161.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4039 | 4221 | +4.5% | -155.5 to +520.7 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 20.44 | 16.43 | -19.6% | -5.475 to -2.543 | GAIN |
| failed requests (%) | 7.527 | 6.734 | -10.5% | -1.529 to -0.05581 | GAIN |
| HPA replicas, mean | 9.534 | 14.04 | +47.3% | +4.149 to +4.863 | power given |
| pods started | 5.707 | 12.07 | +111.5% | +5.883 to +6.848 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.934e-16 to -2.98e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.1 | 179.6 | -0.3% | -0.8684 to -0.182 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.1 | 179.6 | -0.3% | -0.8684 to -0.182 | GAIN |
| CPU used with Omni's own (cores), mean | 1.934 | 1.974 | +2.1% | +0.02861 to +0.05128 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.75 | 59.22 | +2.6% | +1.17 to +1.782 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1368 | 1319 | -3.6% | -248.7 to +149.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4155 | 4444 | +6.9% | -303.7 to +880.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 24.05 | 18.74 | -22.1% | -6.959 to -3.654 | GAIN |
| failed requests (%) | 10.43 | 9.121 | -12.5% | -2.05 to -0.5609 | GAIN |
| HPA replicas, mean | 9.654 | 13.89 | +43.9% | +3.853 to +4.621 | power given |
| pods started | 4.854 | 11.66 | +140.2% | +6.142 to +7.468 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.223e-16 to +8.905e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.8 | 181.2 | -0.4% | -1.12 to -0.1881 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.8 | 181.2 | -0.4% | -1.12 to -0.1881 | GAIN |
| CPU used with Omni's own (cores), mean | 2.087 | 2.129 | +2.0% | +0.02904 to +0.0554 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.36 | 63.97 | +2.6% | +1.23 to +1.992 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.09024 | +0.0902 | +0.07842 to +0.1021 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Energy / Facility / Industrial

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
