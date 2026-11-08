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
| response time (ms), 95th percentile | 1589 | 1389 | 1142 | 1285 | 1792 | 1497 | 1437 | 1353 | 1446 | 1564 | 1484 | 1649 | 1267 | 1442 |
| response time (ms), 99th percentile | 4518 | 4622 | 4220 | 4269 | 5200 | 5069 | 4678 | 4605 | 4533 | 5008 | 4031 | 4410 | 4500 | 4991 |
| time over the response line (% of samples) | 15.95 | 11.83 | 18.97 | 14.17 | 18.91 | 14.67 | 16.18 | 12.82 | 22.68 | 17.09 | 21.57 | 17.21 | 22.1 | 16.79 |
| failed requests (%) | 5.038 | 4.829 | 7.324 | 6.403 | 6.206 | 6.169 | 5.492 | 5.41 | 6.817 | 6.499 | 8.243 | 6.831 | 9.343 | 7.842 |
| HPA replicas, mean | 9.537 | 13.98 | 9.607 | 14.37 | 9.622 | 14.49 | 9.569 | 14.26 | 9.581 | 14.41 | 9.559 | 14.22 | 9.629 | 14.35 |
| pods started | 5.686 | 11.26 | 5.514 | 12.6 | 4.886 | 11.09 | 5.229 | 11.31 | 5.257 | 10.94 | 5.457 | 11.8 | 5.229 | 12.2 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 178.5 | 179.2 | 180.8 | 179.7 | 180.3 | 180.1 | 179 | 179.8 | 181.7 | 180.5 | 180.5 | 179.9 | 181.5 | 180.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.5 | 179.2 | 180.8 | 179.7 | 180.3 | 180.1 | 179 | 179.8 | 181.7 | 180.5 | 180.5 | 179.9 | 181.5 | 180.8 |
| CPU used with Omni's own (cores), mean | 1.837 | 1.884 | 1.972 | 1.999 | 1.992 | 2.041 | 1.886 | 1.938 | 2.087 | 2.128 | 1.979 | 2.021 | 2.056 | 2.092 |
| host CPU busy, the real machine under kind (%) | 54.78 | 56.42 | 58.68 | 59.99 | 59.36 | 60.99 | 56.29 | 58 | 61.98 | 63.53 | 58.89 | 60.56 | 61.25 | 62.89 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.09143 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1589 | 1389 | -12.6% | -426.8 to +25.36 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4518 | 4622 | +2.3% | -196.5 to +402.7 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 15.95 | 11.83 | -25.8% | -5.392 to -2.843 | GAIN |
| failed requests (%) | 5.038 | 4.829 | -4.2% | -0.4905 to +0.07059 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.537 | 13.98 | +46.6% | +3.94 to +4.953 | power given |
| pods started | 5.686 | 11.26 | +98.0% | +5.098 to +6.045 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.797e-16 to +3.812e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.5 | 179.2 | +0.4% | +0.2755 to +1.054 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.5 | 179.2 | +0.4% | +0.2755 to +1.054 | power given |
| CPU used with Omni's own (cores), mean | 1.837 | 1.884 | +2.6% | +0.03396 to +0.06089 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.78 | 56.42 | +3.0% | +1.32 to +1.971 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.984e+05 to +8.007e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.428e-05 to -9.402e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1142 | 1285 | +12.6% | -30.63 to +317.8 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4220 | 4269 | +1.1% | -400.4 to +497.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 18.97 | 14.17 | -25.3% | -6.269 to -3.327 | GAIN |
| failed requests (%) | 7.324 | 6.403 | -12.6% | -1.519 to -0.3225 | GAIN |
| HPA replicas, mean | 9.607 | 14.37 | +49.5% | +4.453 to +5.063 | power given |
| pods started | 5.514 | 12.6 | +128.5% | +6.489 to +7.683 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.852e-16 to +4.852e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 179.7 | -0.6% | -1.458 to -0.689 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 179.7 | -0.6% | -1.458 to -0.689 | GAIN |
| CPU used with Omni's own (cores), mean | 1.972 | 1.999 | +1.4% | +0.01553 to +0.03772 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.68 | 59.99 | +2.2% | +0.9532 to +1.674 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.621e+05 to +8.625e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.149e-05 to -8.145e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1792 | 1497 | -16.5% | -519.7 to -70.42 | GAIN |
| response time (ms), 99th percentile | 5200 | 5069 | -2.5% | -493 to +231 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 18.91 | 14.67 | -22.4% | -5.315 to -3.175 | GAIN |
| failed requests (%) | 6.206 | 6.169 | -0.6% | -0.3725 to +0.2973 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.622 | 14.49 | +50.6% | +4.512 to +5.233 | power given |
| pods started | 4.886 | 11.09 | +126.9% | +5.649 to +6.751 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.378e-16 to +3.348e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.3 | 180.1 | -0.1% | -0.5776 to +0.2703 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.3 | 180.1 | -0.1% | -0.5776 to +0.2703 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.992 | 2.041 | +2.5% | +0.03953 to +0.0586 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.36 | 60.99 | +2.7% | +1.402 to +1.861 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1437 | 1353 | -5.8% | -312.8 to +146 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4678 | 4605 | -1.5% | -494.9 to +350 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.18 | 12.82 | -20.8% | -4.316 to -2.412 | GAIN |
| failed requests (%) | 5.492 | 5.41 | -1.5% | -0.34 to +0.1752 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.569 | 14.26 | +49.0% | +4.325 to +5.046 | power given |
| pods started | 5.229 | 11.31 | +116.4% | +5.563 to +6.608 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.162e-16 to +3.639e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179 | 179.8 | +0.4% | +0.2893 to +1.206 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179 | 179.8 | +0.4% | +0.2893 to +1.206 | power given |
| CPU used with Omni's own (cores), mean | 1.886 | 1.938 | +2.8% | +0.03567 to +0.06916 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.29 | 58 | +3.0% | +1.225 to +2.18 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1446 | 1564 | +8.2% | -98.97 to +334.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4533 | 5008 | +10.5% | +44.93 to +904.2 | LOSS |
| time over the response line (% of samples) | 22.68 | 17.09 | -24.6% | -7.215 to -3.947 | GAIN |
| failed requests (%) | 6.817 | 6.499 | -4.7% | -0.653 to +0.0168 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.581 | 14.41 | +50.4% | +4.47 to +5.191 | power given |
| pods started | 5.257 | 10.94 | +108.2% | +5.047 to +6.324 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.527e-16 to -8.596e-18 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.7 | 180.5 | -0.7% | -1.615 to -0.8426 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.7 | 180.5 | -0.7% | -1.615 to -0.8426 | GAIN |
| CPU used with Omni's own (cores), mean | 2.087 | 2.128 | +2.0% | +0.02964 to +0.0522 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.98 | 63.53 | +2.5% | +1.249 to +1.85 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1484 | 1649 | +11.1% | -45.15 to +373.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4031 | 4410 | +9.4% | +14.35 to +745.4 | LOSS |
| time over the response line (% of samples) | 21.57 | 17.21 | -20.2% | -5.934 to -2.785 | GAIN |
| failed requests (%) | 8.243 | 6.831 | -17.1% | -2.184 to -0.64 | GAIN |
| HPA replicas, mean | 9.559 | 14.22 | +48.8% | +4.345 to +4.985 | power given |
| pods started | 5.457 | 11.8 | +116.2% | +5.725 to +6.96 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.223e-16 to +3.701e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.5 | 179.9 | -0.4% | -1.12 to -0.1995 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.5 | 179.9 | -0.4% | -1.12 to -0.1995 | GAIN |
| CPU used with Omni's own (cores), mean | 1.979 | 2.021 | +2.1% | +0.03004 to +0.05454 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.89 | 60.56 | +2.8% | +1.365 to +1.98 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1267 | 1442 | +13.8% | -57.97 to +407.4 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4500 | 4991 | +10.9% | +87.01 to +894.1 | LOSS |
| time over the response line (% of samples) | 22.1 | 16.79 | -24.0% | -7.225 to -3.394 | GAIN |
| failed requests (%) | 9.343 | 7.842 | -16.1% | -2.52 to -0.4821 | GAIN |
| HPA replicas, mean | 9.629 | 14.35 | +49.1% | +4.473 to +4.979 | power given |
| pods started | 5.229 | 12.2 | +133.3% | +6.351 to +7.592 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.153e-16 to +1.585e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.5 | 180.8 | -0.4% | -1.171 to -0.2102 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.5 | 180.8 | -0.4% | -1.171 to -0.2102 | GAIN |
| CPU used with Omni's own (cores), mean | 2.056 | 2.092 | +1.8% | +0.02567 to +0.04765 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.25 | 62.89 | +2.7% | +1.377 to +1.907 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.09143 | +0.0914 | +0.0786 to +0.1043 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
