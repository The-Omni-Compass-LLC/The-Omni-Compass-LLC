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
| response time (ms), 95th percentile | 1748 | 1323 | 1208 | 1462 | 1871 | 1924 | 1446 | 1180 | 1694 | 1541 | 1825 | 1797 | 1565 | 1644 |
| response time (ms), 99th percentile | 4997 | 4600 | 4492 | 4520 | 5853 | 5436 | 4641 | 4292 | 4622 | 4421 | 5119 | 5045 | 5141 | 5252 |
| time over the response line (% of samples) | 17.42 | 13.29 | 21.4 | 17.65 | 21.64 | 16.49 | 16.47 | 12.01 | 22.93 | 18.1 | 25.45 | 19.71 | 26.11 | 20.95 |
| failed requests (%) | 5.721 | 5.606 | 9.128 | 8.006 | 7.359 | 7.126 | 5.502 | 4.859 | 7.569 | 7.156 | 9.725 | 7.65 | 11.42 | 10.35 |
| HPA replicas, mean | 9.569 | 14.01 | 9.628 | 14.26 | 9.648 | 14.29 | 9.574 | 14.16 | 9.604 | 14.19 | 9.634 | 14.5 | 9.678 | 14.42 |
| pods started | 5.229 | 11.37 | 5.143 | 12.2 | 4.486 | 10.49 | 5.143 | 10.89 | 4.857 | 11.23 | 4.714 | 11.46 | 4.771 | 11.54 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.2 | 179.5 | 181.3 | 180.7 | 180.6 | 181 | 179.1 | 179.8 | 181.3 | 180.6 | 181.9 | 180.8 | 182.2 | 181.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.2 | 179.5 | 181.3 | 180.7 | 180.6 | 181 | 179.1 | 179.8 | 181.3 | 180.6 | 181.9 | 180.8 | 182.2 | 181.8 |
| CPU used with Omni's own (cores), mean | 1.892 | 1.941 | 2.033 | 2.079 | 2.038 | 2.088 | 1.875 | 1.916 | 2.062 | 2.109 | 2.107 | 2.135 | 2.152 | 2.199 |
| host CPU busy, the real machine under kind (%) | 56.53 | 58.04 | 60.47 | 62.13 | 60.55 | 62.14 | 56.18 | 57.51 | 61.32 | 62.9 | 62.51 | 63.95 | 64.13 | 65.95 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.09714 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1748 | 1323 | -24.3% | -693.1 to -156.3 | GAIN |
| response time (ms), 99th percentile | 4997 | 4600 | -7.9% | -860 to +65.78 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 17.42 | 13.29 | -23.7% | -5.356 to -2.907 | GAIN |
| failed requests (%) | 5.721 | 5.606 | -2.0% | -0.4922 to +0.2608 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.569 | 14.01 | +46.4% | +3.936 to +4.946 | power given |
| pods started | 5.229 | 11.37 | +117.5% | +5.497 to +6.789 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.221e-16 to +2.161e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.2 | 179.5 | +0.1% | -0.1121 to +0.6304 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.2 | 179.5 | +0.1% | -0.1121 to +0.6304 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.892 | 1.941 | +2.6% | +0.0352 to +0.06327 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.53 | 58.04 | +2.7% | +1.16 to +1.866 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.972e+05 to +8.008e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.43e-05 to -9.387e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1208 | 1462 | +21.0% | -1.462 to +508.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4492 | 4520 | +0.6% | -484.9 to +540.9 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 21.4 | 17.65 | -17.5% | -5.691 to -1.808 | GAIN |
| failed requests (%) | 9.128 | 8.006 | -12.3% | -1.916 to -0.3272 | GAIN |
| HPA replicas, mean | 9.628 | 14.26 | +48.1% | +4.378 to +4.887 | power given |
| pods started | 5.143 | 12.2 | +137.2% | +6.365 to +7.749 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.332e-16 to +1.795e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.3 | 180.7 | -0.3% | -1.075 to -0.072 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.3 | 180.7 | -0.3% | -1.075 to -0.072 | GAIN |
| CPU used with Omni's own (cores), mean | 2.033 | 2.079 | +2.2% | +0.03122 to +0.05969 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.47 | 62.13 | +2.8% | +1.291 to +2.035 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.623e+05 to +8.628e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.152e-05 to -8.147e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1871 | 1924 | +2.8% | -291.5 to +396.8 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5853 | 5436 | -7.1% | -861.8 to +26.87 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 21.64 | 16.49 | -23.8% | -6.462 to -3.838 | GAIN |
| failed requests (%) | 7.359 | 7.126 | -3.2% | -0.682 to +0.2175 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.648 | 14.29 | +48.1% | +4.225 to +5.057 | power given |
| pods started | 4.486 | 10.49 | +133.8% | +5.405 to +6.595 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.844e-16 to +4.336e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 181 | +0.2% | -0.1336 to +0.8183 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 181 | +0.2% | -0.1336 to +0.8183 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.038 | 2.088 | +2.5% | +0.03899 to +0.0613 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.55 | 62.14 | +2.6% | +1.29 to +1.884 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 4 (response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1446 | 1180 | -18.4% | -542.3 to +10.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4641 | 4292 | -7.5% | -679.6 to -17.67 | GAIN |
| time over the response line (% of samples) | 16.47 | 12.01 | -27.1% | -5.943 to -2.977 | GAIN |
| failed requests (%) | 5.502 | 4.859 | -11.7% | -1.247 to -0.03875 | GAIN |
| HPA replicas, mean | 9.574 | 14.16 | +47.9% | +4.145 to +5.032 | power given |
| pods started | 5.143 | 10.89 | +111.7% | +5.096 to +6.39 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.399e-16 to +8.16e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.1 | 179.8 | +0.4% | +0.2977 to +1.005 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.1 | 179.8 | +0.4% | +0.2977 to +1.005 | power given |
| CPU used with Omni's own (cores), mean | 1.875 | 1.916 | +2.2% | +0.02967 to +0.05342 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.18 | 57.51 | +2.4% | +1.034 to +1.626 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1694 | 1541 | -9.0% | -360.2 to +53.99 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4622 | 4421 | -4.4% | -627.6 to +225.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 22.93 | 18.1 | -21.1% | -6.337 to -3.318 | GAIN |
| failed requests (%) | 7.569 | 7.156 | -5.5% | -0.9964 to +0.1686 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.604 | 14.19 | +47.8% | +4.141 to +5.039 | power given |
| pods started | 4.857 | 11.23 | +131.2% | +5.788 to +6.955 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.295e-16 to -8.41e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.3 | 180.6 | -0.4% | -1.143 to -0.3214 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.3 | 180.6 | -0.4% | -1.143 to -0.3214 | GAIN |
| CPU used with Omni's own (cores), mean | 2.062 | 2.109 | +2.3% | +0.03568 to +0.05781 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.32 | 62.9 | +2.6% | +1.239 to +1.912 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1825 | 1797 | -1.5% | -283.3 to +226.9 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5119 | 5045 | -1.5% | -523.5 to +373.9 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 25.45 | 19.71 | -22.6% | -7.79 to -3.698 | GAIN |
| failed requests (%) | 9.725 | 7.65 | -21.3% | -3.377 to -0.7745 | GAIN |
| HPA replicas, mean | 9.634 | 14.5 | +50.5% | +4.64 to +5.089 | power given |
| pods started | 4.714 | 11.46 | +143.0% | +6.158 to +7.328 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.989e-16 to +3.481e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.9 | 180.8 | -0.6% | -1.502 to -0.7022 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.9 | 180.8 | -0.6% | -1.502 to -0.7022 | GAIN |
| CPU used with Omni's own (cores), mean | 2.107 | 2.135 | +1.3% | +0.01532 to +0.04089 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.51 | 63.95 | +2.3% | +1.079 to +1.803 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1565 | 1644 | +5.1% | -155.7 to +314.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5141 | 5252 | +2.2% | -410.9 to +634 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 26.11 | 20.95 | -19.8% | -7.013 to -3.312 | GAIN |
| failed requests (%) | 11.42 | 10.35 | -9.4% | -2.091 to -0.04806 | GAIN |
| HPA replicas, mean | 9.678 | 14.42 | +49.0% | +4.426 to +5.06 | power given |
| pods started | 4.771 | 11.54 | +141.9% | +6.237 to +7.305 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.078e-16 to +4.8e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 181.8 | -0.3% | -0.9754 to +0.03737 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 181.8 | -0.3% | -0.9754 to +0.03737 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.152 | 2.199 | +2.2% | +0.0337 to +0.0611 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.13 | 65.95 | +2.8% | +1.452 to +2.184 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.09714 | +0.0971 | +0.08699 to +0.1073 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
