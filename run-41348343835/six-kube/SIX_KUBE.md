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
| response time (ms), 95th percentile | 1690 | 1722 | 646.1 | 619.3 | 1604 | 1368 | 2376 | 2611 | 1975 | 1976 | 1558 | 1623 | 1537 | 1869 |
| response time (ms), 99th percentile | 4996 | 4569 | 2574 | 2344 | 4780 | 4458 | 6516 | 6984 | 5449 | 5683 | 4808 | 5398 | 5808 | 5918 |
| time over the response line (% of samples) | 17.47 | 13.56 | 9.818 | 7.288 | 15.06 | 10.75 | 23.26 | 16.6 | 31.3 | 20.95 | 24.68 | 18.78 | 29.69 | 21.85 |
| failed requests (%) | 6.633 | 5.92 | 3.898 | 3.276 | 4.726 | 3.782 | 8.295 | 7.283 | 9.931 | 8.686 | 8.811 | 7.603 | 13.23 | 10.28 |
| HPA replicas, mean | 9.573 | 12.71 | 9.514 | 11.74 | 9.564 | 12.97 | 9.646 | 13.49 | 9.62 | 13.8 | 9.633 | 12.99 | 9.75 | 13.42 |
| pods started | 5.1 | 9.4 | 6.1 | 12.6 | 5.2 | 9.7 | 4.5 | 9.9 | 5.1 | 10 | 5 | 10.3 | 4 | 10 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.1 | 180.1 | 177.1 | 177.4 | 179.1 | 179.5 | 180.4 | 181.3 | 183.6 | 183.1 | 182 | 181.8 | 183.6 | 184 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.1 | 180.1 | 177.1 | 177.4 | 179.1 | 179.5 | 180.4 | 181.3 | 183.6 | 183.1 | 182 | 181.8 | 183.6 | 184 |
| CPU used with Omni's own (cores), mean | 1.899 | 1.912 | 1.645 | 1.651 | 1.858 | 1.857 | 2.064 | 2.08 | 2.269 | 2.26 | 2.121 | 2.132 | 2.304 | 2.291 |
| host CPU busy, the real machine under kind (%) | 56.8 | 57.23 | 49.51 | 49.83 | 55.6 | 55.69 | 61.16 | 61.46 | 66.85 | 66.98 | 62.74 | 63.25 | 68.35 | 68.38 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.23 | 0.1 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1690 | 1722 | +1.9% | -554 to +619.2 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4996 | 4569 | -8.6% | -1239 to +383.9 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 17.47 | 13.56 | -22.4% | -6.025 to -1.791 | GAIN |
| failed requests (%) | 6.633 | 5.92 | -10.8% | -1.438 to +0.01078 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.573 | 12.71 | +32.8% | +1.398 to +4.884 | power given |
| pods started | 5.1 | 9.4 | +84.3% | +2.646 to +5.954 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.294e-15 to -1.267e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.1 | 180.1 | +0.5% | +0.1853 to +1.702 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.1 | 180.1 | +0.5% | +0.1853 to +1.702 | power given |
| CPU used with Omni's own (cores), mean | 1.899 | 1.912 | +0.7% | -0.01358 to +0.03948 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.8 | 57.23 | +0.8% | -0.01096 to +0.8785 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.972e+05 to +7.999e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.419e-05 to -9.388e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 646.1 | 619.3 | -4.2% | -387.1 to +333.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 2574 | 2344 | -8.9% | -612.2 to +152 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 9.818 | 7.288 | -25.8% | -5.217 to +0.1556 | STEADY, inside the noise (cut) |
| failed requests (%) | 3.898 | 3.276 | -16.0% | -1.51 to +0.2662 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.514 | 11.74 | +23.4% | +0.8168 to +3.628 | power given |
| pods started | 6.1 | 12.6 | +106.6% | +4.415 to +8.585 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.115e-15 to +7.599e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 177.1 | 177.4 | +0.2% | -0.4051 to +1.096 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.1 | 177.4 | +0.2% | -0.4051 to +1.096 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.645 | 1.651 | +0.4% | -0.02441 to +0.03717 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 49.51 | 49.83 | +0.7% | -0.8071 to +1.462 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.618e+05 to +8.629e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.153e-05 to -8.143e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1604 | 1368 | -14.7% | -559.1 to +86.64 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4780 | 4458 | -6.7% | -984.5 to +340.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 15.06 | 10.75 | -28.6% | -6.888 to -1.734 | GAIN |
| failed requests (%) | 4.726 | 3.782 | -20.0% | -1.969 to +0.08141 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.564 | 12.97 | +35.6% | +1.703 to +5.101 | power given |
| pods started | 5.2 | 9.7 | +86.5% | +2.772 to +6.228 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.43e-16 to +7.206e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.1 | 179.5 | +0.2% | -0.03562 to +0.8436 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.1 | 179.5 | +0.2% | -0.03562 to +0.8436 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.858 | 1.857 | -0.1% | -0.02603 to +0.02416 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.6 | 55.69 | +0.1% | -0.4742 to +0.6354 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.243e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2376 | 2611 | +9.9% | -300.8 to +770.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6516 | 6984 | +7.2% | -242.1 to +1178 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 23.26 | 16.6 | -28.6% | -9.549 to -3.765 | GAIN |
| failed requests (%) | 8.295 | 7.283 | -12.2% | -2.178 to +0.1538 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.646 | 13.49 | +39.8% | +2.239 to +5.447 | power given |
| pods started | 4.5 | 9.9 | +120.0% | +3.578 to +7.222 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.25e-15 to +3.623e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 181.3 | +0.5% | +0.299 to +1.57 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 181.3 | +0.5% | +0.299 to +1.57 | power given |
| CPU used with Omni's own (cores), mean | 2.064 | 2.08 | +0.8% | -0.006952 to +0.03806 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.16 | 61.46 | +0.5% | -0.1845 to +0.7926 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1975 | 1976 | +0.1% | -407.2 to +409.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5449 | 5683 | +4.3% | -990.5 to +1457 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 31.3 | 20.95 | -33.1% | -14.8 to -5.891 | GAIN |
| failed requests (%) | 9.931 | 8.686 | -12.5% | -2.044 to -0.4469 | GAIN |
| HPA replicas, mean | 9.62 | 13.8 | +43.5% | +2.861 to +5.505 | power given |
| pods started | 5.1 | 10 | +96.1% | +3.452 to +6.348 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.356e-15 to -2.431e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 183.1 | -0.3% | -1.652 to +0.6248 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.6 | 183.1 | -0.3% | -1.652 to +0.6248 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.269 | 2.26 | -0.4% | -0.02343 to +0.005118 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.85 | 66.98 | +0.2% | -0.187 to +0.4455 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.377e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1558 | 1623 | +4.2% | -294.7 to +425.3 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4808 | 5398 | +12.3% | -387.9 to +1567 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 24.68 | 18.78 | -23.9% | -8.873 to -2.912 | GAIN |
| failed requests (%) | 8.811 | 7.603 | -13.7% | -2.569 to +0.1514 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.633 | 12.99 | +34.9% | +1.903 to +4.814 | power given |
| pods started | 5 | 10.3 | +106.0% | +3.79 to +6.81 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.116e-15 to +5.833e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182 | 181.8 | -0.1% | -0.9434 to +0.5765 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182 | 181.8 | -0.1% | -0.9434 to +0.5765 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.121 | 2.132 | +0.5% | -0.004223 to +0.02576 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.74 | 63.25 | +0.8% | -0.009275 to +1.026 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1537 | 1869 | +21.6% | -108.2 to +773.2 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5808 | 5918 | +1.9% | -857.4 to +1077 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 29.69 | 21.85 | -26.4% | -11.44 to -4.255 | GAIN |
| failed requests (%) | 13.23 | 10.28 | -22.3% | -4.978 to -0.9203 | GAIN |
| HPA replicas, mean | 9.75 | 13.42 | +37.7% | +2.925 to +4.424 | power given |
| pods started | 4 | 10 | +150.0% | +4.694 to +7.306 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.063e-16 to +7.286e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 184 | +0.2% | -0.8127 to +1.64 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.6 | 184 | +0.2% | -0.8127 to +1.64 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.304 | 2.291 | -0.6% | -0.04064 to +0.01464 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.35 | 68.38 | +0.0% | -0.5447 to +0.6018 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.984e-09 | power given |
| organism behind its window (s) | 0.23 | 0.1 | -56.5% | -0.6503 to +0.3903 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
