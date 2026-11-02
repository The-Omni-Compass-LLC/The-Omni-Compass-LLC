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
| response time (ms), 95th percentile | 1433 | 1338 | 1472 | 1355 | 1713 | 1496 | 1817 | 1816 | 1838 | 1798 | 1754 | 1594 | 1469 | 1690 |
| response time (ms), 99th percentile | 4480 | 4325 | 4741 | 5023 | 5109 | 4602 | 5741 | 5826 | 5348 | 5463 | 4997 | 5122 | 4928 | 5452 |
| time over the response line (% of samples) | 16.35 | 11.74 | 27.49 | 18.27 | 18.39 | 13.08 | 21.11 | 14.91 | 28.79 | 20.15 | 26.88 | 19.7 | 26.66 | 19.62 |
| failed requests (%) | 5.561 | 4.862 | 11.94 | 9.036 | 6.096 | 5.229 | 7.009 | 6.091 | 9.379 | 8.428 | 10.44 | 8.086 | 11.62 | 9.348 |
| HPA replicas, mean | 9.557 | 12.55 | 9.656 | 12.93 | 9.597 | 13.08 | 9.644 | 13.55 | 9.629 | 13.66 | 9.613 | 12.69 | 9.672 | 13.06 |
| pods started | 5.343 | 9.743 | 5 | 10.09 | 4.914 | 9.771 | 4.743 | 9.6 | 4.771 | 9.657 | 5.143 | 10.06 | 4.943 | 9.771 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 178.6 | 179 | 182.3 | 182.1 | 179.6 | 180 | 180.8 | 181.2 | 182.9 | 182.7 | 182.2 | 181.5 | 182.8 | 182.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.6 | 179 | 182.3 | 182.1 | 179.6 | 180 | 180.8 | 181.2 | 182.9 | 182.7 | 182.2 | 181.5 | 182.8 | 182.3 |
| CPU used with Omni's own (cores), mean | 1.839 | 1.842 | 2.159 | 2.135 | 1.936 | 1.929 | 2.056 | 2.062 | 2.206 | 2.205 | 2.128 | 2.118 | 2.177 | 2.166 |
| host CPU busy, the real machine under kind (%) | 54.95 | 55.11 | 64.03 | 63.73 | 57.74 | 57.65 | 61.06 | 61.24 | 65.21 | 65.54 | 63.02 | 63.08 | 64.7 | 64.93 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.08571 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1433 | 1338 | -6.6% | -323.9 to +135.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4480 | 4325 | -3.5% | -526.8 to +217.5 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.35 | 11.74 | -28.2% | -6.079 to -3.143 | GAIN |
| failed requests (%) | 5.561 | 4.862 | -12.6% | -1.148 to -0.2503 | GAIN |
| HPA replicas, mean | 9.557 | 12.55 | +31.3% | +2.227 to +3.754 | power given |
| pods started | 5.343 | 9.743 | +82.4% | +3.654 to +5.146 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.615e-16 to +1.701e-18 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.6 | 179 | +0.2% | +0.07031 to +0.76 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.6 | 179 | +0.2% | +0.07031 to +0.76 | power given |
| CPU used with Omni's own (cores), mean | 1.839 | 1.842 | +0.2% | -0.00772 to +0.01462 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.95 | 55.11 | +0.3% | -0.1127 to +0.4403 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.976e+05 to +7.988e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.406e-05 to -9.392e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1472 | 1355 | -8.0% | -315.8 to +80.28 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4741 | 5023 | +6.0% | -224.6 to +788.9 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 27.49 | 18.27 | -33.5% | -11.74 to -6.702 | GAIN |
| failed requests (%) | 11.94 | 9.036 | -24.3% | -4.181 to -1.622 | GAIN |
| HPA replicas, mean | 9.656 | 12.93 | +33.9% | +2.654 to +3.885 | power given |
| pods started | 5 | 10.09 | +101.7% | +4.289 to +5.882 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.133e-16 to +3.625e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 182.1 | -0.1% | -0.7335 to +0.2272 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 182.1 | -0.1% | -0.7335 to +0.2272 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.159 | 2.135 | -1.1% | -0.03796 to -0.01006 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.03 | 63.73 | -0.5% | -0.6446 to +0.03332 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.616e+05 to +8.621e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.146e-05 to -8.141e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 4 (response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1713 | 1496 | -12.7% | -483.5 to +49.63 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5109 | 4602 | -9.9% | -867.5 to -147.5 | GAIN |
| time over the response line (% of samples) | 18.39 | 13.08 | -28.9% | -6.75 to -3.865 | GAIN |
| failed requests (%) | 6.096 | 5.229 | -14.2% | -1.425 to -0.3089 | GAIN |
| HPA replicas, mean | 9.597 | 13.08 | +36.3% | +2.779 to +4.191 | power given |
| pods started | 4.914 | 9.771 | +98.8% | +4.062 to +5.652 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.255e-16 to +3.27e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.6 | 180 | +0.2% | +0.05412 to +0.668 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.6 | 180 | +0.2% | +0.05412 to +0.668 | power given |
| CPU used with Omni's own (cores), mean | 1.936 | 1.929 | -0.3% | -0.016 to +0.002822 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.74 | 57.65 | -0.2% | -0.3561 to +0.1679 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.243e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1817 | 1816 | -0.1% | -325.8 to +322.9 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5741 | 5826 | +1.5% | -243.8 to +412.7 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 21.11 | 14.91 | -29.4% | -7.418 to -4.993 | GAIN |
| failed requests (%) | 7.009 | 6.091 | -13.1% | -1.28 to -0.5561 | GAIN |
| HPA replicas, mean | 9.644 | 13.55 | +40.5% | +3.314 to +4.498 | power given |
| pods started | 4.743 | 9.6 | +102.4% | +4.028 to +5.687 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.74e-16 to +2.694e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 181.2 | +0.2% | +0.07044 to +0.7737 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 181.2 | +0.2% | +0.07044 to +0.7737 | power given |
| CPU used with Omni's own (cores), mean | 2.056 | 2.062 | +0.3% | -0.004249 to +0.0167 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.06 | 61.24 | +0.3% | -0.01556 to +0.3776 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1838 | 1798 | -2.2% | -230 to +150.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5348 | 5463 | +2.1% | -378.2 to +607.9 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 28.79 | 20.15 | -30.0% | -10.46 to -6.812 | GAIN |
| failed requests (%) | 9.379 | 8.428 | -10.1% | -1.295 to -0.6063 | GAIN |
| HPA replicas, mean | 9.629 | 13.66 | +41.9% | +3.443 to +4.623 | power given |
| pods started | 4.771 | 9.657 | +102.4% | +4.033 to +5.738 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.139e-16 to +3.139e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 182.9 | 182.7 | -0.1% | -0.6208 to +0.2753 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 182.7 | -0.1% | -0.6208 to +0.2753 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.206 | 2.205 | -0.0% | -0.008606 to +0.007345 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.21 | 65.54 | +0.5% | +0.1176 to +0.5449 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1754 | 1594 | -9.1% | -404 to +83.99 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4997 | 5122 | +2.5% | -342.5 to +591.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 26.88 | 19.7 | -26.7% | -9.116 to -5.237 | GAIN |
| failed requests (%) | 10.44 | 8.086 | -22.6% | -3.521 to -1.19 | GAIN |
| HPA replicas, mean | 9.613 | 12.69 | +32.0% | +2.399 to +3.748 | power given |
| pods started | 5.143 | 10.06 | +95.6% | +4.246 to +5.583 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.926e-16 to +5.464e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 181.5 | -0.4% | -1.11 to -0.3067 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 181.5 | -0.4% | -1.11 to -0.3067 | GAIN |
| CPU used with Omni's own (cores), mean | 2.128 | 2.118 | -0.5% | -0.02068 to +0.0007692 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.02 | 63.08 | +0.1% | -0.2199 to +0.3504 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1469 | 1690 | +15.0% | -8.604 to +450 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4928 | 5452 | +10.7% | +85.26 to +964.5 | LOSS |
| time over the response line (% of samples) | 26.66 | 19.62 | -26.4% | -9.269 to -4.809 | GAIN |
| failed requests (%) | 11.62 | 9.348 | -19.5% | -3.261 to -1.279 | GAIN |
| HPA replicas, mean | 9.672 | 13.06 | +35.0% | +2.833 to +3.939 | power given |
| pods started | 4.943 | 9.771 | +97.7% | +4.225 to +5.432 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.405e-16 to +3.898e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.8 | 182.3 | -0.3% | -1.04 to +0.006262 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.8 | 182.3 | -0.3% | -1.04 to +0.006262 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.177 | 2.166 | -0.5% | -0.02448 to +0.002447 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.7 | 64.93 | +0.4% | -0.08946 to +0.5529 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.08571 | +0.0857 | +0.07352 to +0.09791 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
