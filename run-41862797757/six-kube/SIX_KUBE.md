# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on: native | The spine, the muscles every stack runs on: omni | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1605 | 1444 | 1166 | 1237 | 1491 | 1526 | 1735 | 1842 | 1283 | 1416 | 1444 | 1500 | 1396 | 1434 |
| response time (ms), 99th percentile | 5020 | 5277 | 4408 | 4381 | 5245 | 5357 | 6072 | 5943 | 3946 | 4015 | 4307 | 4577 | 5288 | 5370 |
| time over the response line (% of samples) | 19.01 | 14.46 | 20.8 | 15.57 | 19.87 | 15.13 | 22.39 | 16.96 | 20.91 | 16 | 20.67 | 17.11 | 23.48 | 17.65 |
| failed requests (%) | 6.518 | 6.2 | 8.537 | 7.192 | 6.681 | 6.044 | 7.665 | 7.305 | 6.48 | 6.303 | 7.793 | 6.846 | 9.681 | 8.358 |
| HPA replicas, mean | 9.605 | 14.58 | 9.613 | 14.4 | 9.614 | 14.43 | 9.696 | 14.51 | 9.543 | 13.88 | 9.566 | 14.07 | 9.667 | 14.38 |
| pods started | 5.029 | 11.06 | 5.629 | 11.77 | 5.057 | 10.97 | 3.914 | 10.14 | 5.343 | 11.09 | 5.371 | 11.66 | 4.714 | 11.66 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.9 | 180.4 | 180.9 | 180 | 180.6 | 180.5 | 181 | 181.6 | 180.3 | 179.7 | 180.7 | 179.8 | 182.1 | 181.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.9 | 180.4 | 180.9 | 180 | 180.6 | 180.5 | 181 | 181.6 | 180.3 | 179.7 | 180.7 | 179.8 | 182.1 | 181.2 |
| CPU used with Omni's own (cores), mean | 1.968 | 2.015 | 2.01 | 2.038 | 2.015 | 2.065 | 2.075 | 2.122 | 1.963 | 2.006 | 1.99 | 2.021 | 2.113 | 2.152 |
| host CPU busy, the real machine under kind (%) | 58.43 | 60.14 | 59.88 | 61.05 | 60.07 | 61.82 | 61.59 | 63.11 | 58.59 | 60.16 | 59 | 60.49 | 63.04 | 64.5 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.09143 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1605 | 1444 | -10.1% | -381.4 to +57.99 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5020 | 5277 | +5.1% | -165 to +678 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 19.01 | 14.46 | -23.9% | -5.763 to -3.332 | GAIN |
| failed requests (%) | 6.518 | 6.2 | -4.9% | -0.6109 to -0.02462 | GAIN |
| HPA replicas, mean | 9.605 | 14.58 | +51.9% | +4.751 to +5.21 | power given |
| pods started | 5.029 | 11.06 | +119.9% | +5.652 to +6.406 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.12e-16 to -3.06e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.9 | 180.4 | +0.3% | -0.04815 to +0.9968 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.9 | 180.4 | +0.3% | -0.04815 to +0.9968 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.968 | 2.015 | +2.4% | +0.03728 to +0.05711 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.43 | 60.14 | +2.9% | +1.477 to +1.939 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.983e+05 to +7.992e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.411e-05 to -9.4e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1166 | 1237 | +6.1% | -102.6 to +245.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4408 | 4381 | -0.6% | -513.7 to +460.1 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 20.8 | 15.57 | -25.2% | -7.138 to -3.336 | GAIN |
| failed requests (%) | 8.537 | 7.192 | -15.8% | -2.149 to -0.5425 | GAIN |
| HPA replicas, mean | 9.613 | 14.4 | +49.8% | +4.553 to +5.012 | power given |
| pods started | 5.629 | 11.77 | +109.1% | +5.663 to +6.622 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.188e-16 to +4.203e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 180 | -0.5% | -1.347 to -0.5157 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 180 | -0.5% | -1.347 to -0.5157 | GAIN |
| CPU used with Omni's own (cores), mean | 2.01 | 2.038 | +1.4% | +0.01317 to +0.04325 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.88 | 61.05 | +1.9% | +0.7223 to +1.604 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.62e+05 to +8.625e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.149e-05 to -8.145e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1491 | 1526 | +2.4% | -238.6 to +309.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5245 | 5357 | +2.1% | -472.5 to +695.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 19.87 | 15.13 | -23.9% | -6.158 to -3.327 | GAIN |
| failed requests (%) | 6.681 | 6.044 | -9.5% | -1.257 to -0.0157 | GAIN |
| HPA replicas, mean | 9.614 | 14.43 | +50.1% | +4.415 to +5.213 | power given |
| pods started | 5.057 | 10.97 | +116.9% | +5.353 to +6.475 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.711e-16 to -4.098e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 180.5 | -0.0% | -0.5639 to +0.4674 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 180.5 | -0.0% | -0.5639 to +0.4674 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.015 | 2.065 | +2.5% | +0.03618 to +0.06453 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.07 | 61.82 | +2.9% | +1.428 to +2.082 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1735 | 1842 | +6.2% | -202 to +416.5 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6072 | 5943 | -2.1% | -567.7 to +309.9 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 22.39 | 16.96 | -24.3% | -6.613 to -4.249 | GAIN |
| failed requests (%) | 7.665 | 7.305 | -4.7% | -0.7165 to -0.003984 | GAIN |
| HPA replicas, mean | 9.696 | 14.51 | +49.7% | +4.431 to +5.203 | power given |
| pods started | 3.914 | 10.14 | +159.1% | +5.651 to +6.806 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.441e-16 to +4.979e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 181.6 | +0.3% | +0.1131 to +1.058 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 181.6 | +0.3% | +0.1131 to +1.058 | power given |
| CPU used with Omni's own (cores), mean | 2.075 | 2.122 | +2.2% | +0.03424 to +0.05887 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.59 | 63.11 | +2.5% | +1.242 to +1.791 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1283 | 1416 | +10.3% | -117.1 to +381.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3946 | 4015 | +1.7% | -404.8 to +542.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 20.91 | 16 | -23.5% | -6.636 to -3.178 | GAIN |
| failed requests (%) | 6.48 | 6.303 | -2.7% | -0.4331 to +0.07901 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.543 | 13.88 | +45.5% | +3.761 to +4.916 | power given |
| pods started | 5.343 | 11.09 | +107.5% | +5.182 to +6.304 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.622e-16 to +2.592e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.3 | 179.7 | -0.4% | -1.102 to -0.2748 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.3 | 179.7 | -0.4% | -1.102 to -0.2748 | GAIN |
| CPU used with Omni's own (cores), mean | 1.963 | 2.006 | +2.2% | +0.02959 to +0.05711 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.59 | 60.16 | +2.7% | +1.193 to +1.96 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1444 | 1500 | +3.8% | -148.7 to +259.5 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4307 | 4577 | +6.3% | -178.4 to +718.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 20.67 | 17.11 | -17.2% | -4.844 to -2.265 | GAIN |
| failed requests (%) | 7.793 | 6.846 | -12.2% | -1.652 to -0.2429 | GAIN |
| HPA replicas, mean | 9.566 | 14.07 | +47.1% | +4.165 to +4.841 | power given |
| pods started | 5.371 | 11.66 | +117.0% | +5.81 to +6.761 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.402e-16 to +2.356e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 179.8 | -0.5% | -1.332 to -0.4967 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 179.8 | -0.5% | -1.332 to -0.4967 | GAIN |
| CPU used with Omni's own (cores), mean | 1.99 | 2.021 | +1.6% | +0.01943 to +0.04289 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59 | 60.49 | +2.5% | +1.223 to +1.758 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1396 | 1434 | +2.7% | -155 to +231.3 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5288 | 5370 | +1.6% | -446.4 to +610.9 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 23.48 | 17.65 | -24.8% | -7.994 to -3.661 | GAIN |
| failed requests (%) | 9.681 | 8.358 | -13.7% | -2.247 to -0.4007 | GAIN |
| HPA replicas, mean | 9.667 | 14.38 | +48.7% | +4.455 to +4.964 | power given |
| pods started | 4.714 | 11.66 | +147.3% | +6.354 to +7.532 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.073e-16 to +1.998e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.1 | 181.2 | -0.5% | -1.379 to -0.5227 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.1 | 181.2 | -0.5% | -1.379 to -0.5227 | GAIN |
| CPU used with Omni's own (cores), mean | 2.113 | 2.152 | +1.8% | +0.0266 to +0.05082 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.04 | 64.5 | +2.3% | +1.111 to +1.813 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.09143 | +0.0914 | +0.08167 to +0.1012 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
