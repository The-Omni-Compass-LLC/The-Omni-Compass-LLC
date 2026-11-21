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
| response time (ms), 95th percentile | 1526 | 1306 | 1577 | 1544 | 1614 | 1347 | 1548 | 1424 | 1462 | 1333 | 1989 | 1759 | 1656 | 1449 |
| response time (ms), 99th percentile | 5037 | 4513 | 5022 | 5111 | 4481 | 4362 | 4720 | 4734 | 3933 | 4032 | 4823 | 5059 | 4835 | 5235 |
| time over the response line (% of samples) | 15.37 | 11.1 | 28.28 | 18.7 | 16.17 | 12.16 | 16.65 | 12 | 22.09 | 16.04 | 30.69 | 21.91 | 27.22 | 18.54 |
| failed requests (%) | 4.407 | 4.018 | 12.04 | 9.565 | 5.475 | 5.125 | 5.542 | 5.008 | 7.144 | 6.41 | 12.33 | 9.881 | 11.37 | 9.493 |
| HPA replicas, mean | 9.581 | 13.18 | 9.657 | 13.01 | 9.563 | 12.76 | 9.573 | 12.92 | 9.55 | 12.81 | 9.648 | 13.28 | 9.659 | 12.67 |
| pods started | 5.486 | 10.06 | 5.143 | 10.26 | 5.457 | 9.286 | 5.486 | 9.486 | 5.371 | 9.457 | 4.829 | 9.743 | 5.114 | 10.11 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.3 | 178.9 | 181.8 | 181.8 | 179.3 | 178.5 | 179.7 | 178.7 | 180 | 179.9 | 182 | 182 | 181.5 | 181.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.3 | 178.9 | 181.8 | 181.8 | 179.3 | 178.5 | 179.7 | 178.7 | 180 | 179.9 | 182 | 182 | 181.5 | 181.6 |
| CPU used with Omni's own (cores), mean | 1.901 | 1.902 | 2.165 | 2.15 | 1.873 | 1.879 | 1.908 | 1.909 | 1.986 | 1.98 | 2.189 | 2.178 | 2.143 | 2.137 |
| host CPU busy, the real machine under kind (%) | 56.48 | 56.61 | 64.03 | 64.08 | 55.94 | 56.2 | 56.81 | 56.99 | 58.82 | 59.28 | 64.71 | 65.03 | 63.44 | 63.72 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.07714 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 6 (response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1526 | 1306 | -14.4% | -511.2 to +71.99 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5037 | 4513 | -10.4% | -955.4 to -92.54 | GAIN |
| time over the response line (% of samples) | 15.37 | 11.1 | -27.8% | -5.364 to -3.177 | GAIN |
| failed requests (%) | 4.407 | 4.018 | -8.8% | -0.7468 to -0.0319 | GAIN |
| HPA replicas, mean | 9.581 | 13.18 | +37.5% | +2.901 to +4.291 | power given |
| pods started | 5.486 | 10.06 | +83.3% | +3.793 to +5.35 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.843e-16 to +2.813e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.3 | 178.9 | -0.3% | -0.9248 to -0.01925 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.3 | 178.9 | -0.3% | -0.9248 to -0.01925 | GAIN |
| CPU used with Omni's own (cores), mean | 1.901 | 1.902 | +0.1% | -0.01195 to +0.01494 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.48 | 56.61 | +0.2% | -0.1864 to +0.4327 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.956e+05 to +7.986e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.403e-05 to -9.369e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1577 | 1544 | -2.1% | -215.3 to +149.3 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5022 | 5111 | +1.8% | -436.8 to +613.7 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 28.28 | 18.7 | -33.9% | -11.99 to -7.171 | GAIN |
| failed requests (%) | 12.04 | 9.565 | -20.6% | -3.535 to -1.419 | GAIN |
| HPA replicas, mean | 9.657 | 13.01 | +34.7% | +2.755 to +3.945 | power given |
| pods started | 5.143 | 10.26 | +99.4% | +4.291 to +5.938 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.561e-16 to +3.038e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.8 | 181.8 | -0.0% | -0.4747 to +0.3377 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.8 | 181.8 | -0.0% | -0.4747 to +0.3377 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.165 | 2.15 | -0.7% | -0.02826 to -0.001953 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.03 | 64.08 | +0.1% | -0.282 to +0.3825 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.617e+05 to +8.622e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.146e-05 to -8.142e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (response time (ms), 95th percentile; time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1614 | 1347 | -16.5% | -512.2 to -22.11 | GAIN |
| response time (ms), 99th percentile | 4481 | 4362 | -2.7% | -470.9 to +232.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 16.17 | 12.16 | -24.8% | -5.34 to -2.683 | GAIN |
| failed requests (%) | 5.475 | 5.125 | -6.4% | -0.7799 to +0.08145 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.563 | 12.76 | +33.4% | +2.374 to +4.01 | power given |
| pods started | 5.457 | 9.286 | +70.2% | +2.841 to +4.816 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.141e-16 to -9.79e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.3 | 178.5 | -0.4% | -1.238 to -0.311 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.3 | 178.5 | -0.4% | -1.238 to -0.311 | GAIN |
| CPU used with Omni's own (cores), mean | 1.873 | 1.879 | +0.3% | -0.003413 to +0.0148 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.94 | 56.2 | +0.5% | -0.00438 to +0.5285 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1548 | 1424 | -8.0% | -461.3 to +212.2 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4720 | 4734 | +0.3% | -376.8 to +403.4 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 16.65 | 12 | -27.9% | -5.888 to -3.418 | GAIN |
| failed requests (%) | 5.542 | 5.008 | -9.6% | -0.8876 to -0.1812 | GAIN |
| HPA replicas, mean | 9.573 | 12.92 | +35.0% | +2.58 to +4.112 | power given |
| pods started | 5.486 | 9.486 | +72.9% | +3.13 to +4.87 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.217e-16 to +1.634e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.7 | 178.7 | -0.5% | -1.46 to -0.5102 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.7 | 178.7 | -0.5% | -1.46 to -0.5102 | GAIN |
| CPU used with Omni's own (cores), mean | 1.908 | 1.909 | +0.1% | -0.01068 to +0.01418 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.81 | 56.99 | +0.3% | -0.1211 to +0.4745 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1462 | 1333 | -8.8% | -350.3 to +93.54 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 3933 | 4032 | +2.5% | -318.7 to +516.4 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 22.09 | 16.04 | -27.4% | -7.965 to -4.133 | GAIN |
| failed requests (%) | 7.144 | 6.41 | -10.3% | -1.147 to -0.3218 | GAIN |
| HPA replicas, mean | 9.55 | 12.81 | +34.2% | +2.48 to +4.047 | power given |
| pods started | 5.371 | 9.457 | +76.1% | +3.124 to +5.048 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.839e-16 to +3.332e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180 | 179.9 | -0.0% | -0.492 to +0.3272 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180 | 179.9 | -0.0% | -0.492 to +0.3272 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.986 | 1.98 | -0.3% | -0.01466 to +0.003547 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.82 | 59.28 | +0.8% | +0.1322 to +0.7907 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.377e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1989 | 1759 | -11.5% | -477.2 to +18.76 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4823 | 5059 | +4.9% | -260 to +731.7 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 30.69 | 21.91 | -28.6% | -10.84 to -6.711 | GAIN |
| failed requests (%) | 12.33 | 9.881 | -19.9% | -3.353 to -1.544 | GAIN |
| HPA replicas, mean | 9.648 | 13.28 | +37.6% | +2.941 to +4.316 | power given |
| pods started | 4.829 | 9.743 | +101.8% | +4.035 to +5.793 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.556e-16 to +1.988e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182 | 182 | -0.0% | -0.4092 to +0.3235 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182 | 182 | -0.0% | -0.4092 to +0.3235 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.189 | 2.178 | -0.5% | -0.02196 to +0.001752 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.71 | 65.03 | +0.5% | -0.03125 to +0.6611 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1656 | 1449 | -12.5% | -375.5 to -37.73 | GAIN |
| response time (ms), 99th percentile | 4835 | 5235 | +8.3% | -177.2 to +976.3 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 27.22 | 18.54 | -31.9% | -10.95 to -6.413 | GAIN |
| failed requests (%) | 11.37 | 9.493 | -16.5% | -2.738 to -1.026 | GAIN |
| HPA replicas, mean | 9.659 | 12.67 | +31.2% | +2.431 to +3.589 | power given |
| pods started | 5.114 | 10.11 | +97.8% | +4.184 to +5.816 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.983e-16 to +2.416e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.5 | 181.6 | +0.0% | -0.3607 to +0.5071 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.5 | 181.6 | +0.0% | -0.3607 to +0.5071 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.143 | 2.137 | -0.3% | -0.02021 to +0.007833 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.44 | 63.72 | +0.4% | -0.06056 to +0.6258 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.07714 | +0.0771 | +0.06251 to +0.09178 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
