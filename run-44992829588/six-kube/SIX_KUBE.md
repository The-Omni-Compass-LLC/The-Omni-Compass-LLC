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
| response time (ms), 95th percentile | 1266 | 1052 | 1252 | 1401 | 1123 | 1050 | 1419 | 1440 | 1337 | 1279 | 1336 | 1406 | 1098 | 1170 |
| response time (ms), 99th percentile | 3993 | 4170 | 4129 | 4491 | 4369 | 4185 | 5072 | 4945 | 4172 | 4411 | 3865 | 4116 | 4176 | 4387 |
| time over the response line (% of samples) | 13.32 | 9.629 | 20.27 | 16.25 | 14.41 | 10.3 | 16.03 | 12.02 | 19.5 | 14.6 | 19.89 | 16.31 | 19.1 | 14.91 |
| failed requests (%) | 3.459 | 3.284 | 8.2 | 7.414 | 4.084 | 3.664 | 4.403 | 4.169 | 5.613 | 5.448 | 7.338 | 6.302 | 7.614 | 6.835 |
| HPA replicas, mean | 9.565 | 14.46 | 9.606 | 14.27 | 9.555 | 14.11 | 9.61 | 14.47 | 9.554 | 14.32 | 9.557 | 14.26 | 9.614 | 14.18 |
| pods started | 5.457 | 11.97 | 5.6 | 12.49 | 5.714 | 11.03 | 5.171 | 11.49 | 5.514 | 11.37 | 5.657 | 12.09 | 5.229 | 12.6 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 178.6 | 179 | 180.7 | 180.3 | 178.8 | 179.2 | 179.9 | 180 | 181 | 180 | 180.3 | 179.8 | 180.6 | 180 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.6 | 179 | 180.7 | 180.3 | 178.8 | 179.2 | 179.9 | 180 | 181 | 180 | 180.3 | 179.8 | 180.6 | 180 |
| CPU used with Omni's own (cores), mean | 1.82 | 1.881 | 1.991 | 2.038 | 1.845 | 1.895 | 1.936 | 1.985 | 2.007 | 2.045 | 1.942 | 1.998 | 1.98 | 2.021 |
| host CPU busy, the real machine under kind (%) | 54.86 | 56.62 | 59.48 | 61.37 | 55.39 | 56.96 | 57.75 | 59.42 | 59.99 | 61.55 | 58.31 | 60.3 | 59.22 | 61.05 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.002857 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1266 | 1052 | -16.9% | -443.9 to +17.25 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3993 | 4170 | +4.4% | -175.7 to +529.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 13.32 | 9.629 | -27.7% | -4.683 to -2.7 | GAIN |
| failed requests (%) | 3.459 | 3.284 | -5.1% | -0.6193 to +0.2698 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.565 | 14.46 | +51.1% | +4.666 to +5.117 | power given |
| pods started | 5.457 | 11.97 | +119.4% | +6.129 to +6.899 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.339e-16 to +1.756e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.6 | 179 | +0.2% | -0.05751 to +0.7633 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.6 | 179 | +0.2% | -0.05751 to +0.7633 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.82 | 1.881 | +3.3% | +0.04857 to +0.07171 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.86 | 56.62 | +3.2% | +1.469 to +2.036 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.988e+05 to +8.015e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.438e-05 to -9.406e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1252 | 1401 | +11.8% | -70.89 to +367.6 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4129 | 4491 | +8.8% | -106.7 to +830.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 20.27 | 16.25 | -19.8% | -5.471 to -2.569 | GAIN |
| failed requests (%) | 8.2 | 7.414 | -9.6% | -1.528 to -0.04471 | GAIN |
| HPA replicas, mean | 9.606 | 14.27 | +48.5% | +4.355 to +4.965 | power given |
| pods started | 5.6 | 12.49 | +123.0% | +6.286 to +7.485 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.882e-16 to -2.791e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 180.3 | -0.2% | -0.9099 to +0.1231 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 180.3 | -0.2% | -0.9099 to +0.1231 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.991 | 2.038 | +2.3% | +0.03301 to +0.06054 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.48 | 61.37 | +3.2% | +1.554 to +2.223 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.623e+05 to +8.628e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.152e-05 to -8.147e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1123 | 1050 | -6.5% | -275 to +128.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4369 | 4185 | -4.2% | -580.7 to +213.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 14.41 | 10.3 | -28.5% | -5.157 to -3.065 | GAIN |
| failed requests (%) | 4.084 | 3.664 | -10.3% | -0.807 to -0.03203 | GAIN |
| HPA replicas, mean | 9.555 | 14.11 | +47.7% | +4.026 to +5.08 | power given |
| pods started | 5.714 | 11.03 | +93.0% | +4.709 to +5.919 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.461e-16 to +1.908e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.8 | 179.2 | +0.2% | -0.07281 to +0.7235 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.8 | 179.2 | +0.2% | -0.07281 to +0.7235 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.845 | 1.895 | +2.7% | +0.03888 to +0.06023 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.39 | 56.96 | +2.8% | +1.31 to +1.837 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1419 | 1440 | +1.5% | -255.6 to +298.6 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5072 | 4945 | -2.5% | -512.8 to +258.9 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.03 | 12.02 | -25.0% | -4.907 to -3.118 | GAIN |
| failed requests (%) | 4.403 | 4.169 | -5.3% | -0.5462 to +0.07886 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.61 | 14.47 | +50.6% | +4.467 to +5.256 | power given |
| pods started | 5.171 | 11.49 | +122.1% | +5.891 to +6.737 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.039e-15 to -1.791e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.9 | 180 | +0.1% | -0.2996 to +0.6229 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.9 | 180 | +0.1% | -0.2996 to +0.6229 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.936 | 1.985 | +2.5% | +0.03884 to +0.05958 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.75 | 59.42 | +2.9% | +1.417 to +1.931 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1337 | 1279 | -4.3% | -184.2 to +69.24 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4172 | 4411 | +5.7% | -136 to +612.6 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 19.5 | 14.6 | -25.1% | -6.415 to -3.392 | GAIN |
| failed requests (%) | 5.613 | 5.448 | -2.9% | -0.4417 to +0.1113 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.554 | 14.32 | +49.9% | +4.309 to +5.232 | power given |
| pods started | 5.514 | 11.37 | +106.2% | +5.291 to +6.423 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.038e-16 to +4.561e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180 | -0.5% | -1.407 to -0.4962 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180 | -0.5% | -1.407 to -0.4962 | GAIN |
| CPU used with Omni's own (cores), mean | 2.007 | 2.045 | +1.9% | +0.02484 to +0.05142 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.99 | 61.55 | +2.6% | +1.223 to +1.895 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1336 | 1406 | +5.2% | -111.5 to +250.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3865 | 4116 | +6.5% | -211.3 to +714.3 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 19.89 | 16.31 | -18.0% | -4.853 to -2.307 | GAIN |
| failed requests (%) | 7.338 | 6.302 | -14.1% | -1.788 to -0.2839 | GAIN |
| HPA replicas, mean | 9.557 | 14.26 | +49.2% | +4.415 to +4.98 | power given |
| pods started | 5.657 | 12.09 | +113.6% | +6.018 to +6.839 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.493e-16 to +1.417e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.3 | 179.8 | -0.3% | -0.9696 to -0.02442 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.3 | 179.8 | -0.3% | -0.9696 to -0.02442 | GAIN |
| CPU used with Omni's own (cores), mean | 1.942 | 1.998 | +2.9% | +0.04357 to +0.06925 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.31 | 60.3 | +3.4% | +1.588 to +2.399 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1098 | 1170 | +6.5% | -144.5 to +287.5 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4176 | 4387 | +5.1% | -221.4 to +643.7 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 19.1 | 14.91 | -22.0% | -5.533 to -2.86 | GAIN |
| failed requests (%) | 7.614 | 6.835 | -10.2% | -1.312 to -0.245 | GAIN |
| HPA replicas, mean | 9.614 | 14.18 | +47.5% | +4.213 to +4.919 | power given |
| pods started | 5.229 | 12.6 | +141.0% | +6.794 to +7.949 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.229e-16 to -8.914e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 180 | -0.4% | -1.056 to -0.2442 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 180 | -0.4% | -1.056 to -0.2442 | GAIN |
| CPU used with Omni's own (cores), mean | 1.98 | 2.021 | +2.1% | +0.02979 to +0.05202 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.22 | 61.05 | +3.1% | +1.527 to +2.138 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.002857 | +0.00286 | -0.002949 to +0.008663 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
