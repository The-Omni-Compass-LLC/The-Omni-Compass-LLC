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
| response time (ms), 95th percentile | 1213 | 1118 | 1251 | 1411 | 1529 | 1277 | 1223 | 1067 | 1614 | 1544 | 1359 | 1453 | 1099 | 1173 |
| response time (ms), 99th percentile | 4135 | 4263 | 4800 | 4919 | 4615 | 4461 | 4523 | 4090 | 4946 | 5476 | 4623 | 4779 | 4096 | 4287 |
| time over the response line (% of samples) | 13.19 | 9.616 | 22.22 | 18.41 | 16.37 | 11.96 | 15.12 | 11.03 | 23.23 | 18.35 | 19.93 | 16.26 | 18.31 | 14.18 |
| failed requests (%) | 3.389 | 3.052 | 8.745 | 8.507 | 5.336 | 4.709 | 4.85 | 4.543 | 6.888 | 6.67 | 6.935 | 6.136 | 7.311 | 6.39 |
| HPA replicas, mean | 9.545 | 14.13 | 9.647 | 14.64 | 9.589 | 14.39 | 9.584 | 14.14 | 9.605 | 14.4 | 9.578 | 14.27 | 9.61 | 14.15 |
| pods started | 5.829 | 11.69 | 5.343 | 11.74 | 5.314 | 11.09 | 5.2 | 11.43 | 5.114 | 11.26 | 5.257 | 11.54 | 5.429 | 12.69 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 178.6 | 179.1 | 181.9 | 181.1 | 179.6 | 179.9 | 178.6 | 179.2 | 182.4 | 181.8 | 180.7 | 180.2 | 180.7 | 180 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.6 | 179.1 | 181.9 | 181.1 | 179.6 | 179.9 | 178.6 | 179.2 | 182.4 | 181.8 | 180.7 | 180.2 | 180.7 | 180 |
| CPU used with Omni's own (cores), mean | 1.818 | 1.864 | 2.11 | 2.157 | 1.919 | 1.965 | 1.844 | 1.894 | 2.146 | 2.19 | 1.997 | 2.041 | 1.973 | 2.003 |
| host CPU busy, the real machine under kind (%) | 54.53 | 56.06 | 62.75 | 64.73 | 57.55 | 59.24 | 55.57 | 57.22 | 63.85 | 65.32 | 59.47 | 61.21 | 58.94 | 60.53 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1213 | 1118 | -7.8% | -292.1 to +102.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4135 | 4263 | +3.1% | -179.1 to +435.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 13.19 | 9.616 | -27.1% | -4.628 to -2.528 | GAIN |
| failed requests (%) | 3.389 | 3.052 | -9.9% | -0.6191 to -0.05526 | GAIN |
| HPA replicas, mean | 9.545 | 14.13 | +48.0% | +4.151 to +5.022 | power given |
| pods started | 5.829 | 11.69 | +100.5% | +5.363 to +6.351 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.308e-16 to +2.233e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.6 | 179.1 | +0.2% | +0.00852 to +0.8736 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.6 | 179.1 | +0.2% | +0.00852 to +0.8736 | power given |
| CPU used with Omni's own (cores), mean | 1.818 | 1.864 | +2.5% | +0.03142 to +0.06014 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.53 | 56.06 | +2.8% | +1.158 to +1.891 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.975e+05 to +8.002e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.423e-05 to -9.39e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1251 | 1411 | +12.8% | -44.31 to +365.2 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4800 | 4919 | +2.5% | -335.1 to +571.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 22.22 | 18.41 | -17.1% | -5.591 to -2.026 | GAIN |
| failed requests (%) | 8.745 | 8.507 | -2.7% | -1.177 to +0.702 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.647 | 14.64 | +51.7% | +4.781 to +5.196 | power given |
| pods started | 5.343 | 11.74 | +119.8% | +5.84 to +6.96 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.815e-16 to -1.843e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.9 | 181.1 | -0.4% | -1.188 to -0.4164 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.9 | 181.1 | -0.4% | -1.188 to -0.4164 | GAIN |
| CPU used with Omni's own (cores), mean | 2.11 | 2.157 | +2.2% | +0.03304 to +0.06044 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.75 | 64.73 | +3.2% | +1.656 to +2.299 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.623e+05 to +8.628e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.152e-05 to -8.148e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1529 | 1277 | -16.5% | -459.5 to -46.03 | GAIN |
| response time (ms), 99th percentile | 4615 | 4461 | -3.3% | -573.8 to +265.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.37 | 11.96 | -26.9% | -5.931 to -2.879 | GAIN |
| failed requests (%) | 5.336 | 4.709 | -11.7% | -1.369 to +0.1162 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.589 | 14.39 | +50.1% | +4.409 to +5.202 | power given |
| pods started | 5.314 | 11.09 | +108.6% | +5.264 to +6.279 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.128e-16 to +3.113e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.6 | 179.9 | +0.1% | -0.1868 to +0.6889 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.6 | 179.9 | +0.1% | -0.1868 to +0.6889 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.919 | 1.965 | +2.4% | +0.0341 to +0.05914 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.55 | 59.24 | +2.9% | +1.364 to +2.02 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 4 (response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1223 | 1067 | -12.8% | -416.3 to +104.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4523 | 4090 | -9.6% | -815.6 to -51.89 | GAIN |
| time over the response line (% of samples) | 15.12 | 11.03 | -27.0% | -5.429 to -2.751 | GAIN |
| failed requests (%) | 4.85 | 4.543 | -6.3% | -0.6002 to -0.01493 | GAIN |
| HPA replicas, mean | 9.584 | 14.14 | +47.5% | +4.125 to +4.988 | power given |
| pods started | 5.2 | 11.43 | +119.8% | +5.701 to +6.756 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.521e-16 to +4.002e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.6 | 179.2 | +0.3% | +0.1616 to +0.9169 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.6 | 179.2 | +0.3% | +0.1616 to +0.9169 | power given |
| CPU used with Omni's own (cores), mean | 1.844 | 1.894 | +2.7% | +0.03753 to +0.06248 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.57 | 57.22 | +3.0% | +1.297 to +2.01 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1614 | 1544 | -4.3% | -230.5 to +90.68 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4946 | 5476 | +10.7% | +145.3 to +913.6 | LOSS |
| time over the response line (% of samples) | 23.23 | 18.35 | -21.0% | -6.118 to -3.641 | GAIN |
| failed requests (%) | 6.888 | 6.67 | -3.2% | -0.575 to +0.1397 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.605 | 14.4 | +49.9% | +4.317 to +5.276 | power given |
| pods started | 5.114 | 11.26 | +120.1% | +5.476 to +6.81 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.352e-16 to +1.276e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.4 | 181.8 | -0.3% | -1.022 to -0.2494 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.4 | 181.8 | -0.3% | -1.022 to -0.2494 | GAIN |
| CPU used with Omni's own (cores), mean | 2.146 | 2.19 | +2.0% | +0.03213 to +0.05573 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.85 | 65.32 | +2.3% | +1.066 to +1.884 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1359 | 1453 | +7.0% | -100.4 to +290 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4623 | 4779 | +3.4% | -267 to +578.6 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 19.93 | 16.26 | -18.4% | -4.853 to -2.488 | GAIN |
| failed requests (%) | 6.935 | 6.136 | -11.5% | -1.511 to -0.0866 | GAIN |
| HPA replicas, mean | 9.578 | 14.27 | +49.0% | +4.394 to +4.995 | power given |
| pods started | 5.257 | 11.54 | +119.6% | +5.705 to +6.866 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.413e-16 to +2.352e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 180.2 | -0.3% | -0.868 to -0.08889 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 180.2 | -0.3% | -0.868 to -0.08889 | GAIN |
| CPU used with Omni's own (cores), mean | 1.997 | 2.041 | +2.2% | +0.03414 to +0.05411 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.47 | 61.21 | +2.9% | +1.426 to +2.053 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1099 | 1173 | +6.7% | -129.6 to +277.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4096 | 4287 | +4.7% | -286.7 to +668.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 18.31 | 14.18 | -22.5% | -5.416 to -2.839 | GAIN |
| failed requests (%) | 7.311 | 6.39 | -12.6% | -1.467 to -0.376 | GAIN |
| HPA replicas, mean | 9.61 | 14.15 | +47.2% | +4.188 to +4.894 | power given |
| pods started | 5.429 | 12.69 | +133.7% | +6.709 to +7.806 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.62e-16 to +1.037e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 180 | -0.4% | -1.173 to -0.2241 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 180 | -0.4% | -1.173 to -0.2241 | GAIN |
| CPU used with Omni's own (cores), mean | 1.973 | 2.003 | +1.5% | +0.02123 to +0.03909 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.94 | 60.53 | +2.7% | +1.392 to +1.805 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
