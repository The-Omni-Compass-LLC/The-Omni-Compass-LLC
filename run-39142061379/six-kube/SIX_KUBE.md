# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on: native | The spine, the muscles every stack runs on: omni | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1431 | 1122 | 1196 | 1036 | 2000 | 1872 | 1962 | 1687 | 1966 | 1837 | 2033 | 2110 | 1398 | 1352 |
| response time (ms), 99th percentile | 4077 | 3753 | 3212 | 3477 | 5859 | 5660 | 5517 | 5304 | 5048 | 4907 | 5511 | 5775 | 4952 | 4811 |
| time over the response line (% of samples) | 13.65 | 10.27 | 20.61 | 14.04 | 20.99 | 15.47 | 19.82 | 14.84 | 28.3 | 21.05 | 33.72 | 24.92 | 22.79 | 16.4 |
| failed requests (%) | 4.535 | 4.618 | 9.333 | 7.754 | 7.358 | 6.596 | 6.433 | 6.013 | 9.85 | 8.905 | 14.07 | 11.75 | 9.155 | 7.749 |
| HPA replicas, mean | 9.531 | 12.22 | 9.596 | 11.85 | 9.628 | 13.42 | 9.616 | 13.14 | 9.612 | 13.5 | 9.656 | 13.69 | 9.669 | 13.48 |
| pods started | 5.75 | 8.75 | 5.5 | 9.2 | 5 | 9.4 | 5 | 9.35 | 5.05 | 9.6 | 5.05 | 9.95 | 4.9 | 10.95 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 178.2 | 177.7 | 179.8 | 179.5 | 181.4 | 180.2 | 180.4 | 179.8 | 182.2 | 181.6 | 182.9 | 183.1 | 181.7 | 181.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.2 | 177.7 | 179.8 | 179.5 | 181.4 | 180.2 | 180.4 | 179.8 | 182.2 | 181.6 | 182.9 | 183.1 | 181.7 | 181.6 |
| CPU used with Omni's own (cores), mean | 1.782 | 1.793 | 1.941 | 1.932 | 2.05 | 2.05 | 1.977 | 1.995 | 2.156 | 2.153 | 2.295 | 2.295 | 2.114 | 2.11 |
| host CPU busy, the real machine under kind (%) | 53.11 | 53.39 | 57.86 | 58.04 | 60.79 | 60.83 | 58.59 | 59 | 63.66 | 64.19 | 67.49 | 68.04 | 63.74 | 64.27 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.085 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1431 | 1122 | -21.6% | -543.8 to -75.26 | GAIN |
| response time (ms), 99th percentile | 4077 | 3753 | -7.9% | -689.2 to +41.01 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 13.65 | 10.27 | -24.8% | -4.938 to -1.822 | GAIN |
| failed requests (%) | 4.535 | 4.618 | +1.8% | -0.2368 to +0.4025 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.531 | 12.22 | +28.2% | +1.531 to +3.844 | power given |
| pods started | 5.75 | 8.75 | +52.2% | +1.73 to +4.27 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.546e-16 to +2.217e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.2 | 177.7 | -0.3% | -1.093 to +0.07272 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.2 | 177.7 | -0.3% | -1.093 to +0.07272 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.782 | 1.793 | +0.6% | -0.0006389 to +0.02288 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 53.11 | 53.39 | +0.5% | -0.01685 to +0.5776 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.967e+05 to +7.997e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.416e-05 to -9.381e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1196 | 1036 | -13.4% | -425.2 to +104.8 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 3212 | 3477 | +8.3% | -326.7 to +857.2 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 20.61 | 14.04 | -31.9% | -9.865 to -3.277 | GAIN |
| failed requests (%) | 9.333 | 7.754 | -16.9% | -2.773 to -0.3863 | GAIN |
| HPA replicas, mean | 9.596 | 11.85 | +23.5% | +1.26 to +3.248 | power given |
| pods started | 5.5 | 9.2 | +67.3% | +2.429 to +4.971 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.167e-16 to +2.614e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 179.5 | -0.2% | -0.9424 to +0.3175 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 179.5 | -0.2% | -0.9424 to +0.3175 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.941 | 1.932 | -0.5% | -0.0246 to +0.006008 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.86 | 58.04 | +0.3% | -0.2148 to +0.574 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.619e+05 to +8.625e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.149e-05 to -8.143e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2000 | 1872 | -6.4% | -629.5 to +373.3 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5859 | 5660 | -3.4% | -644.3 to +247.5 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 20.99 | 15.47 | -26.3% | -7.265 to -3.765 | GAIN |
| failed requests (%) | 7.358 | 6.596 | -10.4% | -1.561 to +0.03709 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.628 | 13.42 | +39.3% | +2.864 to +4.71 | power given |
| pods started | 5 | 9.4 | +88.0% | +3.09 to +5.71 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.103e-16 to +3.55e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 180.2 | -0.6% | -1.794 to -0.5613 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 180.2 | -0.6% | -1.794 to -0.5613 | GAIN |
| CPU used with Omni's own (cores), mean | 2.05 | 2.05 | -0.0% | -0.0143 to +0.01411 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.79 | 60.83 | +0.1% | -0.3762 to +0.4629 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.243e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1962 | 1687 | -14.0% | -709.2 to +159.2 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5517 | 5304 | -3.9% | -810.8 to +385.5 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 19.82 | 14.84 | -25.1% | -6.594 to -3.361 | GAIN |
| failed requests (%) | 6.433 | 6.013 | -6.5% | -1.068 to +0.2274 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.616 | 13.14 | +36.7% | +2.518 to +4.535 | power given |
| pods started | 5 | 9.35 | +87.0% | +2.964 to +5.736 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.951e-16 to +1.621e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 179.8 | -0.3% | -1.297 to +0.06916 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 179.8 | -0.3% | -1.297 to +0.06916 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.977 | 1.995 | +0.9% | +0.003842 to +0.03267 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.59 | 59 | +0.7% | +0.06845 to +0.7372 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1966 | 1837 | -6.6% | -360 to +102 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5048 | 4907 | -2.8% | -619.6 to +337.9 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 28.3 | 21.05 | -25.6% | -9.65 to -4.853 | GAIN |
| failed requests (%) | 9.85 | 8.905 | -9.6% | -1.438 to -0.4504 | GAIN |
| HPA replicas, mean | 9.612 | 13.5 | +40.5% | +2.821 to +4.956 | power given |
| pods started | 5.05 | 9.6 | +90.1% | +3.45 to +5.65 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.08e-16 to +3.639e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 181.6 | -0.4% | -1.317 to -0.001425 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 181.6 | -0.4% | -1.317 to -0.001425 | GAIN |
| CPU used with Omni's own (cores), mean | 2.156 | 2.153 | -0.1% | -0.01539 to +0.009513 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.66 | 64.19 | +0.8% | +0.1513 to +0.9098 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2033 | 2110 | +3.8% | -337.7 to +492.7 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5511 | 5775 | +4.8% | -669.9 to +1198 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 33.72 | 24.92 | -26.1% | -12.05 to -5.557 | GAIN |
| failed requests (%) | 14.07 | 11.75 | -16.5% | -3.951 to -0.6886 | GAIN |
| HPA replicas, mean | 9.656 | 13.69 | +41.8% | +3.184 to +4.881 | power given |
| pods started | 5.05 | 9.95 | +97.0% | +3.965 to +5.835 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.637e-16 to +1.42e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.9 | 183.1 | +0.1% | -0.3307 to +0.8027 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 183.1 | +0.1% | -0.3307 to +0.8027 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.295 | 2.295 | +0.0% | -0.02722 to +0.02762 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.49 | 68.04 | +0.8% | -0.2447 to +1.332 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1398 | 1352 | -3.3% | -418.2 to +326.1 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4952 | 4811 | -2.8% | -943.7 to +661.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 22.79 | 16.4 | -28.0% | -8.428 to -4.343 | GAIN |
| failed requests (%) | 9.155 | 7.749 | -15.4% | -2.425 to -0.3867 | GAIN |
| HPA replicas, mean | 9.669 | 13.48 | +39.4% | +3.073 to +4.539 | power given |
| pods started | 4.9 | 10.95 | +123.5% | +5.185 to +6.915 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.528e-16 to +4.087e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.7 | 181.6 | -0.1% | -0.8081 to +0.5604 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.7 | 181.6 | -0.1% | -0.8081 to +0.5604 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.114 | 2.11 | -0.2% | -0.02237 to +0.01423 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.74 | 64.27 | +0.8% | +0.04776 to +1.011 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.085 | +0.085 | +0.06785 to +0.1021 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
