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
| response time (ms), 95th percentile | 1479 | 1356 | 1297 | 1463 | 1672 | 1308 | 1411 | 1067 | 1574 | 1633 | 910.4 | 919 | 1291 | 1358 |
| response time (ms), 99th percentile | 5156 | 5107 | 4517 | 4687 | 5100 | 4852 | 4421 | 4334 | 4746 | 5032 | 3354 | 3495 | 4392 | 4534 |
| time over the response line (% of samples) | 17.15 | 13.22 | 22.95 | 17.82 | 16.87 | 12.89 | 15.16 | 11.37 | 22.42 | 16.39 | 12 | 9.209 | 21.77 | 17.59 |
| failed requests (%) | 5.258 | 5.099 | 9.571 | 8.496 | 5.179 | 5.138 | 4.795 | 4.729 | 6.821 | 6.405 | 3.878 | 3.265 | 9.197 | 8.082 |
| HPA replicas, mean | 9.594 | 14.6 | 9.649 | 14.25 | 9.591 | 14.15 | 9.548 | 14.18 | 9.609 | 14.45 | 9.511 | 13.84 | 9.654 | 14.21 |
| pods started | 5.229 | 11.23 | 4.8 | 11.86 | 5.171 | 10.89 | 5.6 | 11.03 | 5.114 | 11.5 | 5.657 | 12.23 | 4.829 | 12.4 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180 | 180.5 | 181.4 | 180.6 | 179.7 | 180.3 | 178.8 | 179.4 | 182 | 180.9 | 178.5 | 177.9 | 181.6 | 180.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180 | 180.5 | 181.4 | 180.6 | 179.7 | 180.3 | 178.8 | 179.4 | 182 | 180.9 | 178.5 | 177.9 | 181.6 | 180.8 |
| CPU used with Omni's own (cores), mean | 1.963 | 2.005 | 2.07 | 2.101 | 1.945 | 1.995 | 1.849 | 1.888 | 2.112 | 2.129 | 1.755 | 1.796 | 2.072 | 2.106 |
| host CPU busy, the real machine under kind (%) | 58.37 | 60.02 | 61.5 | 62.83 | 58.07 | 59.61 | 55.33 | 56.61 | 62.54 | 63.65 | 52.65 | 54.29 | 61.7 | 63.23 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.08 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1479 | 1356 | -8.3% | -404.4 to +158.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5156 | 5107 | -1.0% | -474.6 to +376.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 17.15 | 13.22 | -23.0% | -4.834 to -3.04 | GAIN |
| failed requests (%) | 5.258 | 5.099 | -3.0% | -0.4744 to +0.1567 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.594 | 14.6 | +52.2% | +4.782 to +5.231 | power given |
| pods started | 5.229 | 11.23 | +114.8% | +5.5 to +6.5 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.244e-16 to +6.609e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180 | 180.5 | +0.3% | +0.007067 to +0.9405 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180 | 180.5 | +0.3% | +0.007067 to +0.9405 | power given |
| CPU used with Omni's own (cores), mean | 1.963 | 2.005 | +2.1% | +0.0314 to +0.05189 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.37 | 60.02 | +2.8% | +1.443 to +1.863 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.971e+05 to +7.995e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.415e-05 to -9.386e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1297 | 1463 | +12.8% | -82.63 to +415.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4517 | 4687 | +3.8% | -318.6 to +658.3 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 22.95 | 17.82 | -22.4% | -6.799 to -3.463 | GAIN |
| failed requests (%) | 9.571 | 8.496 | -11.2% | -1.816 to -0.3355 | GAIN |
| HPA replicas, mean | 9.649 | 14.25 | +47.7% | +4.219 to +4.992 | power given |
| pods started | 4.8 | 11.86 | +147.0% | +6.396 to +7.718 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.015e-15 to -1.017e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 180.6 | -0.5% | -1.295 to -0.3763 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 180.6 | -0.5% | -1.295 to -0.3763 | GAIN |
| CPU used with Omni's own (cores), mean | 2.07 | 2.101 | +1.5% | +0.01593 to +0.04718 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.5 | 62.83 | +2.2% | +0.9204 to +1.732 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.62e+05 to +8.626e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.15e-05 to -8.145e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1672 | 1308 | -21.8% | -697.5 to -31.11 | GAIN |
| response time (ms), 99th percentile | 5100 | 4852 | -4.9% | -509.6 to +13.85 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.87 | 12.89 | -23.6% | -4.957 to -2.999 | GAIN |
| failed requests (%) | 5.179 | 5.138 | -0.8% | -0.4919 to +0.4098 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.591 | 14.15 | +47.6% | +4.101 to +5.022 | power given |
| pods started | 5.171 | 10.89 | +110.5% | +5.061 to +6.368 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.137e-16 to +7.227e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.7 | 180.3 | +0.3% | +0.1706 to +0.9866 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.7 | 180.3 | +0.3% | +0.1706 to +0.9866 | power given |
| CPU used with Omni's own (cores), mean | 1.945 | 1.995 | +2.6% | +0.04071 to +0.05912 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.07 | 59.61 | +2.7% | +1.283 to +1.805 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1411 | 1067 | -24.4% | -559.8 to -127.4 | GAIN |
| response time (ms), 99th percentile | 4421 | 4334 | -2.0% | -346.7 to +172.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 15.16 | 11.37 | -25.0% | -4.906 to -2.665 | GAIN |
| failed requests (%) | 4.795 | 4.729 | -1.4% | -0.374 to +0.2413 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.548 | 14.18 | +48.6% | +4.201 to +5.07 | power given |
| pods started | 5.6 | 11.03 | +96.9% | +4.92 to +5.937 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.133e-16 to +2.057e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.8 | 179.4 | +0.3% | +0.2147 to +1.017 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.8 | 179.4 | +0.3% | +0.2147 to +1.017 | power given |
| CPU used with Omni's own (cores), mean | 1.849 | 1.888 | +2.2% | +0.02674 to +0.05281 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.33 | 56.61 | +2.3% | +1.012 to +1.541 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

34 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1523 | 1633 | +7.2% | -187.1 to +407 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4688 | 5032 | +7.3% | -204.1 to +892.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 21.87 | 16.39 | -25.1% | -7.138 to -3.822 | GAIN |
| failed requests (%) | 6.638 | 6.405 | -3.5% | -0.921 to +0.4541 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.608 | 14.45 | +50.4% | +4.482 to +5.21 | power given |
| pods started | 5.118 | 11.5 | +124.7% | +5.769 to +6.996 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.549e-16 to -8.999e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.9 | 180.9 | -0.5% | -1.497 to -0.4912 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.9 | 180.9 | -0.5% | -1.497 to -0.4912 | GAIN |
| CPU used with Omni's own (cores), mean | 2.1 | 2.129 | +1.4% | +0.01729 to +0.04009 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.24 | 63.65 | +2.3% | +1.103 to +1.722 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 910.4 | 919 | +0.9% | -172.3 to +189.5 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3354 | 3495 | +4.2% | -259.7 to +542 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 12 | 9.209 | -23.3% | -4.046 to -1.537 | GAIN |
| failed requests (%) | 3.878 | 3.265 | -15.8% | -1.243 to +0.01607 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.511 | 13.84 | +45.5% | +3.951 to +4.709 | power given |
| pods started | 5.657 | 12.23 | +116.2% | +6.113 to +7.03 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.472e-16 to +2.426e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.5 | 177.9 | -0.3% | -1.036 to -0.072 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.5 | 177.9 | -0.3% | -1.036 to -0.072 | GAIN |
| CPU used with Omni's own (cores), mean | 1.755 | 1.796 | +2.4% | +0.0302 to +0.05261 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 52.65 | 54.29 | +3.1% | +1.277 to +2.002 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1291 | 1358 | +5.1% | -90.07 to +222.3 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4392 | 4534 | +3.2% | -279.8 to +564.8 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 21.77 | 17.59 | -19.2% | -5.632 to -2.742 | GAIN |
| failed requests (%) | 9.197 | 8.082 | -12.1% | -1.812 to -0.4184 | GAIN |
| HPA replicas, mean | 9.654 | 14.21 | +47.2% | +4.245 to +4.859 | power given |
| pods started | 4.829 | 12.4 | +156.8% | +7.113 to +8.03 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.74e-16 to +6.5e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.6 | 180.8 | -0.4% | -1.277 to -0.2793 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.6 | 180.8 | -0.4% | -1.277 to -0.2793 | GAIN |
| CPU used with Omni's own (cores), mean | 2.072 | 2.106 | +1.6% | +0.0231 to +0.04515 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.7 | 63.23 | +2.5% | +1.194 to +1.858 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.08 | +0.08 | +0.06606 to +0.09394 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
