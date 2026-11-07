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
| response time (ms), 95th percentile | 1205 | 990.9 | 1168 | 1310 | 1716 | 1653 | 1270 | 1267 | 1478 | 1442 | 1301 | 1402 |
| response time (ms), 99th percentile | 3910 | 3874 | 4001 | 4320 | 5293 | 5465 | 4371 | 4244 | 4046 | 4122 | 4837 | 5239 |
| time over the response line (% of samples) | 12.62 | 9.399 | 20.14 | 15.69 | 19.83 | 15.08 | 14.71 | 11.23 | 22 | 17.71 | 22.69 | 17.77 |
| failed requests (%) | 3.835 | 3.627 | 8.181 | 7.218 | 6.416 | 6.26 | 4.582 | 4.16 | 8.095 | 7.265 | 9.069 | 8.094 |
| HPA replicas, mean | 9.53 | 13.82 | 9.595 | 14.2 | 9.604 | 14.42 | 9.566 | 14.15 | 9.561 | 14.12 | 9.657 | 14.31 |
| pods started | 5.61 | 11.29 | 5.659 | 12 | 5.244 | 11.27 | 5.268 | 11.49 | 5.341 | 11.49 | 5.171 | 12.02 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 177.6 | 178.1 | 180.7 | 179.9 | 180.5 | 180.9 | 178.7 | 179.2 | 180.2 | 180.1 | 182.2 | 181.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.6 | 178.1 | 180.7 | 179.9 | 180.5 | 180.9 | 178.7 | 179.2 | 180.2 | 180.1 | 182.2 | 181.5 |
| CPU used with Omni's own (cores), mean | 1.74 | 1.777 | 1.994 | 2.028 | 2.019 | 2.066 | 1.836 | 1.88 | 1.97 | 2.012 | 2.13 | 2.166 |
| host CPU busy, the real machine under kind (%) | 52.05 | 53.5 | 59.41 | 60.75 | 60.05 | 61.67 | 54.97 | 56.42 | 58.69 | 60.2 | 63.35 | 64.89 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.09268 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1205 | 990.9 | -17.8% | -373.5 to -55.31 | GAIN |
| response time (ms), 99th percentile | 3910 | 3874 | -0.9% | -489.1 to +416.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 12.62 | 9.399 | -25.5% | -4.244 to -2.193 | GAIN |
| failed requests (%) | 3.835 | 3.627 | -5.4% | -0.4932 to +0.07641 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.53 | 13.82 | +45.0% | +3.821 to +4.766 | power given |
| pods started | 5.61 | 11.29 | +101.3% | +5.207 to +6.159 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.707e-16 to +1.674e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 177.6 | 178.1 | +0.3% | +0.1909 to +0.8394 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.6 | 178.1 | +0.3% | +0.1909 to +0.8394 | power given |
| CPU used with Omni's own (cores), mean | 1.74 | 1.777 | +2.1% | +0.02747 to +0.0468 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 52.05 | 53.5 | +2.8% | +1.148 to +1.754 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.98e+05 to +8.004e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.425e-05 to -9.397e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1168 | 1310 | +12.2% | -48.88 to +333.2 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4001 | 4320 | +8.0% | -173 to +811.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 20.14 | 15.69 | -22.1% | -5.969 to -2.93 | GAIN |
| failed requests (%) | 8.181 | 7.218 | -11.8% | -1.621 to -0.3052 | GAIN |
| HPA replicas, mean | 9.595 | 14.2 | +48.0% | +4.295 to +4.908 | power given |
| pods started | 5.659 | 12 | +112.1% | +5.82 to +6.863 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.552e-16 to +5.304e-18 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 179.9 | -0.4% | -1.144 to -0.2714 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 179.9 | -0.4% | -1.144 to -0.2714 | GAIN |
| CPU used with Omni's own (cores), mean | 1.994 | 2.028 | +1.7% | +0.0228 to +0.04515 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.41 | 60.75 | +2.3% | +1.046 to +1.639 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.621e+05 to +8.625e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.149e-05 to -8.145e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1716 | 1653 | -3.7% | -367.1 to +240.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5293 | 5465 | +3.2% | -192.5 to +536.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 19.83 | 15.08 | -24.0% | -5.863 to -3.646 | GAIN |
| failed requests (%) | 6.416 | 6.26 | -2.4% | -0.4991 to +0.1881 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.604 | 14.42 | +50.1% | +4.48 to +5.15 | power given |
| pods started | 5.244 | 11.27 | +114.9% | +5.554 to +6.495 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.303e-16 to +3.869e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.5 | 180.9 | +0.2% | -0.05284 to +0.8326 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.5 | 180.9 | +0.2% | -0.05284 to +0.8326 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.019 | 2.066 | +2.4% | +0.03816 to +0.05687 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.05 | 61.67 | +2.7% | +1.395 to +1.841 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1270 | 1267 | -0.3% | -224.8 to +217.6 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4371 | 4244 | -2.9% | -398 to +144.3 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 14.71 | 11.23 | -23.7% | -4.463 to -2.494 | GAIN |
| failed requests (%) | 4.582 | 4.16 | -9.2% | -0.7608 to -0.08257 | GAIN |
| HPA replicas, mean | 9.566 | 14.15 | +47.9% | +4.249 to +4.918 | power given |
| pods started | 5.268 | 11.49 | +118.1% | +5.68 to +6.759 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.755e-16 to +1.423e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.7 | 179.2 | +0.3% | +0.1285 to +0.892 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.7 | 179.2 | +0.3% | +0.1285 to +0.892 | power given |
| CPU used with Omni's own (cores), mean | 1.836 | 1.88 | +2.4% | +0.03283 to +0.05388 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.97 | 56.42 | +2.6% | +1.145 to +1.738 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1478 | 1442 | -2.4% | -218.9 to +148.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4046 | 4122 | +1.9% | -290.5 to +443.3 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 22 | 17.71 | -19.5% | -5.734 to -2.843 | GAIN |
| failed requests (%) | 8.095 | 7.265 | -10.3% | -1.506 to -0.1561 | GAIN |
| HPA replicas, mean | 9.561 | 14.12 | +47.7% | +4.227 to +4.896 | power given |
| pods started | 5.341 | 11.49 | +115.1% | +5.649 to +6.643 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.404e-16 to -3.294e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.2 | 180.1 | -0.1% | -0.5711 to +0.1992 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.2 | 180.1 | -0.1% | -0.5711 to +0.1992 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.97 | 2.012 | +2.1% | +0.03075 to +0.052 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.69 | 60.2 | +2.6% | +1.211 to +1.819 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1301 | 1402 | +7.7% | -77.49 to +278.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4837 | 5239 | +8.3% | -164.5 to +969.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 22.69 | 17.77 | -21.7% | -6.108 to -3.744 | GAIN |
| failed requests (%) | 9.069 | 8.094 | -10.8% | -1.466 to -0.4838 | GAIN |
| HPA replicas, mean | 9.657 | 14.31 | +48.2% | +4.331 to +4.977 | power given |
| pods started | 5.171 | 12.02 | +132.5% | +6.332 to +7.375 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.492e-16 to -7e-19 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 181.5 | -0.4% | -1.12 to -0.3593 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 181.5 | -0.4% | -1.12 to -0.3593 | GAIN |
| CPU used with Omni's own (cores), mean | 2.13 | 2.166 | +1.7% | +0.02551 to +0.04607 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.35 | 64.89 | +2.4% | +1.278 to +1.784 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.09268 | +0.0927 | +0.08177 to +0.1036 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Distribution / Specialized

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
