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
| response time (ms), 95th percentile | 1370 | 1306 | 1590 | 1589 | 1354 | 1436 | 1519 | 1265 | 1367 | 1405 | 1628 | 1580 | 1454 | 1417 |
| response time (ms), 99th percentile | 4712 | 4502 | 5122 | 5606 | 4696 | 4606 | 5376 | 4930 | 4132 | 4225 | 4739 | 4735 | 4933 | 4969 |
| time over the response line (% of samples) | 16.14 | 12.39 | 26.45 | 20.26 | 15.96 | 12.3 | 17.14 | 13.28 | 21.06 | 16.93 | 24.11 | 18.82 | 21.76 | 16.38 |
| failed requests (%) | 5.327 | 5.184 | 11.4 | 9.947 | 5.116 | 4.701 | 5.436 | 5.278 | 6.726 | 6.587 | 9.119 | 7.447 | 8.534 | 7.206 |
| HPA replicas, mean | 9.553 | 14.08 | 9.668 | 14.52 | 9.565 | 13.86 | 9.595 | 14.21 | 9.547 | 13.78 | 9.608 | 14.35 | 9.651 | 14.35 |
| pods started | 5.543 | 11.69 | 4.971 | 11.34 | 5.371 | 11.31 | 5.235 | 10.79 | 5.429 | 11.46 | 5.086 | 11.6 | 5 | 11.8 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 178.6 | 178.7 | 182.6 | 182 | 179.1 | 178.7 | 179.5 | 179.7 | 180.5 | 179.8 | 181.7 | 180.8 | 181.5 | 180.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.6 | 178.7 | 182.6 | 182 | 179.1 | 178.7 | 179.5 | 179.7 | 180.5 | 179.8 | 181.7 | 180.8 | 181.5 | 180.8 |
| CPU used with Omni's own (cores), mean | 1.84 | 1.877 | 2.184 | 2.217 | 1.869 | 1.901 | 1.923 | 1.965 | 1.974 | 2.011 | 2.084 | 2.117 | 2.062 | 2.098 |
| host CPU busy, the real machine under kind (%) | 54.97 | 56.33 | 64.67 | 66.11 | 55.83 | 57.12 | 57.33 | 58.91 | 58.93 | 60.52 | 61.82 | 63.15 | 61.47 | 63 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.09429 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1370 | 1306 | -4.7% | -233.2 to +105.7 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4712 | 4502 | -4.5% | -612.1 to +191.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.14 | 12.39 | -23.2% | -4.868 to -2.637 | GAIN |
| failed requests (%) | 5.327 | 5.184 | -2.7% | -0.4179 to +0.1326 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.553 | 14.08 | +47.4% | +4.09 to +4.969 | power given |
| pods started | 5.543 | 11.69 | +110.8% | +5.53 to +6.756 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.356e-16 to +5.402e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.6 | 178.7 | +0.0% | -0.3339 to +0.4411 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.6 | 178.7 | +0.0% | -0.3339 to +0.4411 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.84 | 1.877 | +2.0% | +0.02304 to +0.05092 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.97 | 56.33 | +2.5% | +0.9261 to +1.787 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.97e+05 to +7.996e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.415e-05 to -9.385e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1590 | 1589 | -0.1% | -310.6 to +306.9 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5122 | 5606 | +9.4% | +17.35 to +950.5 | LOSS |
| time over the response line (% of samples) | 26.45 | 20.26 | -23.4% | -8.346 to -4.021 | GAIN |
| failed requests (%) | 11.4 | 9.947 | -12.8% | -2.44 to -0.4755 | GAIN |
| HPA replicas, mean | 9.668 | 14.52 | +50.2% | +4.541 to +5.172 | power given |
| pods started | 4.971 | 11.34 | +128.2% | +5.759 to +6.984 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.555e-16 to +9.569e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.6 | 182 | -0.3% | -1.013 to -0.06221 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.6 | 182 | -0.3% | -1.013 to -0.06221 | GAIN |
| CPU used with Omni's own (cores), mean | 2.184 | 2.217 | +1.5% | +0.02013 to +0.045 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.67 | 66.11 | +2.2% | +1.137 to +1.742 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.621e+05 to +8.625e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.15e-05 to -8.145e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1354 | 1436 | +6.0% | -191.8 to +355.4 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4696 | 4606 | -1.9% | -587.9 to +407.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 15.96 | 12.3 | -23.0% | -4.73 to -2.605 | GAIN |
| failed requests (%) | 5.116 | 4.701 | -8.1% | -0.8266 to -0.004111 | GAIN |
| HPA replicas, mean | 9.565 | 13.86 | +44.9% | +3.776 to +4.818 | power given |
| pods started | 5.371 | 11.31 | +110.6% | +5.277 to +6.609 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.803e-16 to +4.818e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.1 | 178.7 | -0.2% | -0.7982 to -0.06408 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.1 | 178.7 | -0.2% | -0.7982 to -0.06408 | GAIN |
| CPU used with Omni's own (cores), mean | 1.869 | 1.901 | +1.7% | +0.02249 to +0.04248 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.83 | 57.12 | +2.3% | +1.056 to +1.528 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

34 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1519 | 1265 | -16.7% | -530.1 to +22.01 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5376 | 4930 | -8.3% | -840.6 to -52.75 | GAIN |
| time over the response line (% of samples) | 17.14 | 13.28 | -22.5% | -4.82 to -2.904 | GAIN |
| failed requests (%) | 5.436 | 5.278 | -2.9% | -0.4436 to +0.1283 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.595 | 14.21 | +48.1% | +4.146 to +5.089 | power given |
| pods started | 5.235 | 10.79 | +106.2% | +4.944 to +6.174 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.567e-16 to +2.432e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.5 | 179.7 | +0.1% | -0.1752 to +0.7044 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.5 | 179.7 | +0.1% | -0.1752 to +0.7044 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.923 | 1.965 | +2.2% | +0.03095 to +0.05279 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.33 | 58.91 | +2.7% | +1.269 to +1.882 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1367 | 1405 | +2.7% | -102.7 to +177.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4132 | 4225 | +2.3% | -246.4 to +432.6 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 21.06 | 16.93 | -19.6% | -5.96 to -2.316 | GAIN |
| failed requests (%) | 6.726 | 6.587 | -2.1% | -0.6426 to +0.364 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.547 | 13.78 | +44.3% | +3.672 to +4.788 | power given |
| pods started | 5.429 | 11.46 | +111.1% | +5.314 to +6.743 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.461e-16 to +1.908e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.5 | 179.8 | -0.4% | -1.059 to -0.2595 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.5 | 179.8 | -0.4% | -1.059 to -0.2595 | GAIN |
| CPU used with Omni's own (cores), mean | 1.974 | 2.011 | +1.9% | +0.02324 to +0.05121 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.93 | 60.52 | +2.7% | +1.223 to +1.96 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1628 | 1580 | -3.0% | -247.6 to +150.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4739 | 4735 | -0.1% | -502.2 to +494.1 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 24.11 | 18.82 | -22.0% | -6.949 to -3.64 | GAIN |
| failed requests (%) | 9.119 | 7.447 | -18.3% | -3.065 to -0.2798 | GAIN |
| HPA replicas, mean | 9.608 | 14.35 | +49.4% | +4.477 to +5.012 | power given |
| pods started | 5.086 | 11.6 | +128.1% | +6.005 to +7.024 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.058e-15 to -1.604e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.7 | 180.8 | -0.5% | -1.374 to -0.5126 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.7 | 180.8 | -0.5% | -1.374 to -0.5126 | GAIN |
| CPU used with Omni's own (cores), mean | 2.084 | 2.117 | +1.6% | +0.02028 to +0.04567 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.82 | 63.15 | +2.2% | +1.005 to +1.659 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1454 | 1417 | -2.6% | -324.7 to +249.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4933 | 4969 | +0.7% | -421 to +492.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 21.76 | 16.38 | -24.7% | -7.41 to -3.359 | GAIN |
| failed requests (%) | 8.534 | 7.206 | -15.6% | -2.21 to -0.4459 | GAIN |
| HPA replicas, mean | 9.651 | 14.35 | +48.7% | +4.436 to +4.964 | power given |
| pods started | 5 | 11.8 | +136.0% | +6.261 to +7.339 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.524e-16 to -1.044e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.5 | 180.8 | -0.4% | -1.143 to -0.2625 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.5 | 180.8 | -0.4% | -1.143 to -0.2625 | GAIN |
| CPU used with Omni's own (cores), mean | 2.062 | 2.098 | +1.7% | +0.01833 to +0.05242 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.47 | 63 | +2.5% | +1.095 to +1.961 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.09429 | +0.0943 | +0.08267 to +0.1059 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
