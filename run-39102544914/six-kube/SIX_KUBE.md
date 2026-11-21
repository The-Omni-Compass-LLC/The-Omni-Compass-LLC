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
| response time (ms), 95th percentile | 1126 | 1483 | 1554 | 1295 | 2494 | 2675 | 1327 | 1145 | 1017 | 840.3 | 1526 | 1709 | 1652 | 1498 |
| response time (ms), 99th percentile | 4706 | 4977 | 4443 | 4190 | 6846 | 6832 | 5056 | 4535 | 2756 | 2624 | 4392 | 4336 | 4745 | 5541 |
| time over the response line (% of samples) | 17.04 | 13.21 | 24.53 | 16.84 | 26.5 | 19.23 | 16.32 | 11.42 | 14.02 | 9.522 | 27.86 | 22.04 | 25.7 | 19.26 |
| failed requests (%) | 6.08 | 5.394 | 10.94 | 8.751 | 9.009 | 8.369 | 4.463 | 4.507 | 4.223 | 4.015 | 11.65 | 10.39 | 11.05 | 10.28 |
| HPA replicas, mean | 9.556 | 13.06 | 9.654 | 12.37 | 9.718 | 14.59 | 9.572 | 13.42 | 9.477 | 11.92 | 9.571 | 12.21 | 9.654 | 13.56 |
| pods started | 5.7 | 9.7 | 5.1 | 9.6 | 4.3 | 10.5 | 5.5 | 10.1 | 5.8 | 9.2 | 5.2 | 9.4 | 4.8 | 9.8 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.9 | 179.2 | 180.9 | 180.5 | 183.7 | 182.7 | 179.4 | 178.7 | 177.8 | 177.4 | 180.8 | 180.5 | 182.2 | 182 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.9 | 179.2 | 180.9 | 180.5 | 183.7 | 182.7 | 179.4 | 178.7 | 177.8 | 177.4 | 180.8 | 180.5 | 182.2 | 182 |
| CPU used with Omni's own (cores), mean | 1.926 | 1.941 | 2.037 | 2.033 | 2.263 | 2.281 | 1.894 | 1.899 | 1.758 | 1.75 | 2.066 | 2.062 | 2.145 | 2.154 |
| host CPU busy, the real machine under kind (%) | 57.13 | 57.54 | 60.61 | 60.73 | 66.82 | 67.23 | 56.26 | 56.54 | 52.79 | 52.89 | 61.01 | 61.37 | 63.6 | 64.3 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.06 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1126 | 1483 | +31.7% | -261 to +975.5 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4706 | 4977 | +5.8% | -431.4 to +973.5 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 17.04 | 13.21 | -22.5% | -6.827 to -0.8255 | GAIN |
| failed requests (%) | 6.08 | 5.394 | -11.3% | -1.844 to +0.473 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.556 | 13.06 | +36.7% | +1.761 to +5.248 | power given |
| pods started | 5.7 | 9.7 | +70.2% | +1.977 to +6.023 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.88e-16 to +6.104e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.9 | 179.2 | -0.4% | -1.727 to +0.3259 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.9 | 179.2 | -0.4% | -1.727 to +0.3259 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.926 | 1.941 | +0.8% | -0.01783 to +0.04903 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.13 | 57.54 | +0.7% | -0.3 to +1.119 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.94e+05 to +8.012e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.435e-05 to -9.35e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1554 | 1295 | -16.6% | -747.9 to +230.9 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4443 | 4190 | -5.7% | -874 to +366.6 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 24.53 | 16.84 | -31.3% | -13.23 to -2.136 | GAIN |
| failed requests (%) | 10.94 | 8.751 | -20.0% | -5.129 to +0.756 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.654 | 12.37 | +28.1% | +1.18 to +4.253 | power given |
| pods started | 5.1 | 9.6 | +88.2% | +2.615 to +6.385 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.494e-16 to +6.718e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 180.5 | -0.2% | -1.057 to +0.4174 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 180.5 | -0.2% | -1.057 to +0.4174 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.037 | 2.033 | -0.2% | -0.02559 to +0.01779 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.61 | 60.73 | +0.2% | -0.5043 to +0.7521 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.618e+05 to +8.626e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.15e-05 to -8.143e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2494 | 2675 | +7.3% | -921.4 to +1285 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6846 | 6832 | -0.2% | -1009 to +980.5 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 26.5 | 19.23 | -27.4% | -9.07 to -5.468 | GAIN |
| failed requests (%) | 9.009 | 8.369 | -7.1% | -1.969 to +0.6878 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.718 | 14.59 | +50.1% | +4.531 to +5.213 | power given |
| pods started | 4.3 | 10.5 | +144.2% | +5.2 to +7.2 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.312e-15 to +6.012e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 182.7 | -0.5% | -1.799 to -0.1297 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 182.7 | -0.5% | -1.799 to -0.1297 | GAIN |
| CPU used with Omni's own (cores), mean | 2.263 | 2.281 | +0.8% | -0.005624 to +0.04082 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.82 | 67.23 | +0.6% | -0.09583 to +0.9004 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.247e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1327 | 1145 | -13.8% | -928.6 to +563.4 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5056 | 4535 | -10.3% | -1498 to +455 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 16.32 | 11.42 | -30.0% | -7.811 to -1.986 | GAIN |
| failed requests (%) | 4.463 | 4.507 | +1.0% | -0.3445 to +0.432 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.572 | 13.42 | +40.2% | +2.368 to +5.328 | power given |
| pods started | 5.5 | 10.1 | +83.6% | +2.841 to +6.359 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.441e-15 to +3.755e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.4 | 178.7 | -0.4% | -1.385 to -0.002206 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.4 | 178.7 | -0.4% | -1.385 to -0.002206 | GAIN |
| CPU used with Omni's own (cores), mean | 1.894 | 1.899 | +0.3% | -0.01204 to +0.02259 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.26 | 56.54 | +0.5% | -0.2064 to +0.7544 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1017 | 840.3 | -17.4% | -324 to -29.67 | GAIN |
| response time (ms), 99th percentile | 2756 | 2624 | -4.8% | -1101 to +837.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 14.02 | 9.522 | -32.1% | -8.403 to -0.6005 | GAIN |
| failed requests (%) | 4.223 | 4.015 | -4.9% | -0.6354 to +0.221 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.477 | 11.92 | +25.7% | +0.7452 to +4.132 | power given |
| pods started | 5.8 | 9.2 | +58.6% | +1.236 to +5.564 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.167e-15 to +6.345e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 177.8 | 177.4 | -0.2% | -1.215 to +0.3362 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.8 | 177.4 | -0.2% | -1.215 to +0.3362 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.758 | 1.75 | -0.4% | -0.03122 to +0.01574 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 52.79 | 52.89 | +0.2% | -0.7143 to +0.9183 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.377e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1526 | 1709 | +11.9% | -385.6 to +749.8 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4392 | 4336 | -1.3% | -856.9 to +745.5 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 27.86 | 22.04 | -20.9% | -10.71 to -0.9477 | GAIN |
| failed requests (%) | 11.65 | 10.39 | -10.8% | -3.023 to +0.5094 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.571 | 12.21 | +27.6% | +0.7621 to +4.515 | power given |
| pods started | 5.2 | 9.4 | +80.8% | +2.947 to +5.453 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.615e-16 to +4.062e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 180.5 | -0.2% | -1.446 to +0.7424 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 180.5 | -0.2% | -1.446 to +0.7424 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.066 | 2.062 | -0.2% | -0.02146 to +0.01357 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.01 | 61.37 | +0.6% | -0.1128 to +0.8349 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1652 | 1498 | -9.3% | -518.5 to +211 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4745 | 5541 | +16.8% | +164 to +1427 | LOSS |
| time over the response line (% of samples) | 25.7 | 19.26 | -25.1% | -10.02 to -2.868 | GAIN |
| failed requests (%) | 11.05 | 10.28 | -7.0% | -1.688 to +0.1399 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.654 | 13.56 | +40.5% | +2.381 to +5.432 | power given |
| pods started | 4.8 | 9.8 | +104.2% | +3.314 to +6.686 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.08e-15 to +1.08e-15 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 182 | -0.1% | -1.31 to +0.8635 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 182 | -0.1% | -1.31 to +0.8635 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.145 | 2.154 | +0.4% | -0.0108 to +0.02885 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.6 | 64.3 | +1.1% | +0.189 to +1.208 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4e+06 to +4.001e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.987e-09 to -4.986e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.06 | +0.06 | +0.02306 to +0.09694 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
