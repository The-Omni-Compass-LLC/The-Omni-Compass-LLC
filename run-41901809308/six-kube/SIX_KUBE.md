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
| response time (ms), 95th percentile | 1479 | 1548 | 1234 | 1397 | 1179 | 1201 | 1751 | 1529 | 1711 | 1845 | 1568 | 1694 | 1497 | 1392 |
| response time (ms), 99th percentile | 5826 | 5285 | 4734 | 4991 | 4878 | 4637 | 5212 | 5547 | 4615 | 4857 | 4882 | 5760 | 4509 | 5046 |
| time over the response line (% of samples) | 17.83 | 13.7 | 23.27 | 17.74 | 16.58 | 12.59 | 20.15 | 15.51 | 26.46 | 20.55 | 22.59 | 18.09 | 23.81 | 17.89 |
| failed requests (%) | 4.885 | 4.747 | 9.573 | 8.339 | 5.22 | 4.731 | 6.361 | 6.272 | 9.012 | 8.194 | 8.056 | 6.947 | 10.55 | 8.666 |
| HPA replicas, mean | 9.633 | 14.6 | 9.639 | 14.5 | 9.607 | 14.48 | 9.606 | 14.43 | 9.611 | 14.18 | 9.601 | 14.66 | 9.669 | 14.29 |
| pods started | 5 | 11.25 | 5.2 | 11.8 | 5.1 | 11.3 | 5.1 | 10.55 | 4.75 | 10.9 | 5 | 10.8 | 4.85 | 12 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 180.3 | 181.9 | 181 | 179.7 | 179.8 | 180.2 | 180.8 | 181.8 | 181 | 181.7 | 181 | 182.4 | 181.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 180.3 | 181.9 | 181 | 179.7 | 179.8 | 180.2 | 180.8 | 181.8 | 181 | 181.7 | 181 | 182.4 | 181.1 |
| CPU used with Omni's own (cores), mean | 1.985 | 2.042 | 2.102 | 2.139 | 1.928 | 1.962 | 2.001 | 2.052 | 2.101 | 2.135 | 2.097 | 2.129 | 2.12 | 2.147 |
| host CPU busy, the real machine under kind (%) | 58.92 | 60.9 | 62.3 | 63.88 | 57.54 | 58.93 | 59.32 | 61.19 | 62.36 | 63.9 | 62.26 | 63.78 | 63.12 | 64.43 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.085 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1479 | 1548 | +4.6% | -279.3 to +416.6 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5826 | 5285 | -9.3% | -1233 to +152.1 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 17.83 | 13.7 | -23.2% | -5.718 to -2.54 | GAIN |
| failed requests (%) | 4.885 | 4.747 | -2.8% | -0.5607 to +0.2851 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.633 | 14.6 | +51.5% | +4.584 to +5.343 | power given |
| pods started | 5 | 11.25 | +125.0% | +5.664 to +6.836 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.244e-16 to +2.803e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 180.3 | -0.1% | -0.7689 to +0.4861 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 180.3 | -0.1% | -0.7689 to +0.4861 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.985 | 2.042 | +2.9% | +0.03588 to +0.07825 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.92 | 60.9 | +3.4% | +1.355 to +2.61 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.977e+05 to +8.02e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.444e-05 to -9.393e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1234 | 1397 | +13.2% | -220 to +545.4 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4734 | 4991 | +5.4% | -229.5 to +742.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 23.27 | 17.74 | -23.8% | -8.156 to -2.914 | GAIN |
| failed requests (%) | 9.573 | 8.339 | -12.9% | -2.405 to -0.06281 | GAIN |
| HPA replicas, mean | 9.639 | 14.5 | +50.5% | +4.559 to +5.17 | power given |
| pods started | 5.2 | 11.8 | +126.9% | +6.004 to +7.196 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.761e-16 to +3.32e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.9 | 181 | -0.5% | -1.431 to -0.3694 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.9 | 181 | -0.5% | -1.431 to -0.3694 | GAIN |
| CPU used with Omni's own (cores), mean | 2.102 | 2.139 | +1.8% | +0.0151 to +0.05887 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.3 | 63.88 | +2.5% | +1.036 to +2.12 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.62e+05 to +8.628e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.152e-05 to -8.144e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1179 | 1201 | +1.9% | -177.8 to +222.2 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4878 | 4637 | -4.9% | -871.8 to +389.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.58 | 12.59 | -24.1% | -5.515 to -2.464 | GAIN |
| failed requests (%) | 5.22 | 4.731 | -9.4% | -1.021 to +0.04277 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.607 | 14.48 | +50.7% | +4.552 to +5.198 | power given |
| pods started | 5.1 | 11.3 | +121.6% | +5.494 to +6.906 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.168e-15 to -1.638e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.7 | 179.8 | +0.0% | -0.5466 to +0.6304 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.7 | 179.8 | +0.0% | -0.5466 to +0.6304 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.928 | 1.962 | +1.8% | +0.01914 to +0.04916 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.54 | 58.93 | +2.4% | +1.117 to +1.656 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1751 | 1529 | -12.7% | -647.8 to +202.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5212 | 5547 | +6.4% | -342.6 to +1012 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 20.15 | 15.51 | -23.0% | -6.132 to -3.148 | GAIN |
| failed requests (%) | 6.361 | 6.272 | -1.4% | -0.9499 to +0.7721 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.606 | 14.43 | +50.2% | +4.279 to +5.365 | power given |
| pods started | 5.1 | 10.55 | +106.9% | +4.797 to +6.103 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.405e-16 to +4.74e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.2 | 180.8 | +0.3% | -0.04936 to +1.279 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.2 | 180.8 | +0.3% | -0.04936 to +1.279 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.001 | 2.052 | +2.5% | +0.03367 to +0.06721 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.32 | 61.19 | +3.2% | +1.585 to +2.155 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1711 | 1845 | +7.8% | -290.6 to +558.3 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4615 | 4857 | +5.2% | -511.4 to +994.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 26.46 | 20.55 | -22.3% | -8.896 to -2.913 | GAIN |
| failed requests (%) | 9.012 | 8.194 | -9.1% | -1.641 to +0.005886 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.611 | 14.18 | +47.5% | +3.957 to +5.182 | power given |
| pods started | 4.75 | 10.9 | +129.5% | +5.387 to +6.913 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.258e-16 to +9.29e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.8 | 181 | -0.4% | -1.293 to -0.3402 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.8 | 181 | -0.4% | -1.293 to -0.3402 | GAIN |
| CPU used with Omni's own (cores), mean | 2.101 | 2.135 | +1.6% | +0.02101 to +0.04776 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.36 | 63.9 | +2.5% | +1.123 to +1.964 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 1

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1568 | 1694 | +8.1% | -183.2 to +436.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4882 | 5760 | +18.0% | +139.2 to +1617 | LOSS |
| time over the response line (% of samples) | 22.59 | 18.09 | -19.9% | -6.536 to -2.47 | GAIN |
| failed requests (%) | 8.056 | 6.947 | -13.8% | -2.109 to -0.1081 | GAIN |
| HPA replicas, mean | 9.601 | 14.66 | +52.7% | +4.747 to +5.372 | power given |
| pods started | 5 | 10.8 | +116.0% | +4.907 to +6.693 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.131e-15 to -2.014e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.7 | 181 | -0.4% | -1.43 to -0.03729 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.7 | 181 | -0.4% | -1.43 to -0.03729 | GAIN |
| CPU used with Omni's own (cores), mean | 2.097 | 2.129 | +1.5% | +0.01987 to +0.04353 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.26 | 63.78 | +2.4% | +1.162 to +1.887 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1497 | 1392 | -7.0% | -304.4 to +95.67 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4509 | 5046 | +11.9% | -316.5 to +1391 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 23.81 | 17.89 | -24.9% | -8.537 to -3.303 | GAIN |
| failed requests (%) | 10.55 | 8.666 | -17.9% | -3.336 to -0.4419 | GAIN |
| HPA replicas, mean | 9.669 | 14.29 | +47.8% | +4.192 to +5.049 | power given |
| pods started | 4.85 | 12 | +147.4% | +6.274 to +8.026 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.951e-16 to +1.621e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.4 | 181.1 | -0.7% | -1.807 to -0.7395 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.4 | 181.1 | -0.7% | -1.807 to -0.7395 | GAIN |
| CPU used with Omni's own (cores), mean | 2.12 | 2.147 | +1.3% | +0.008066 to +0.04693 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.12 | 64.43 | +2.1% | +0.7038 to +1.912 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.085 | +0.085 | +0.06785 to +0.1021 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
