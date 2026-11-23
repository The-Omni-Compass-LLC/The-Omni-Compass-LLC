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
| response time (ms), 95th percentile | 1319 | 1005 | 1280 | 1490 | 1454 | 1261 | 1352 | 1089 | 1508 | 1706 | 1590 | 1538 | 1393 | 1742 |
| response time (ms), 99th percentile | 4335 | 3977 | 4951 | 5232 | 4808 | 4575 | 4703 | 4618 | 4682 | 5089 | 4882 | 4809 | 4589 | 4954 |
| time over the response line (% of samples) | 14.17 | 10.54 | 23.31 | 17.98 | 17.21 | 12.84 | 15.17 | 11.21 | 22.58 | 17.62 | 21.92 | 17.68 | 26.19 | 21.76 |
| failed requests (%) | 3.966 | 4.063 | 9.553 | 8.423 | 5.668 | 5.429 | 4.53 | 4.26 | 6.772 | 6.386 | 7.929 | 6.504 | 11.2 | 10.34 |
| HPA replicas, mean | 9.532 | 13.97 | 9.641 | 14.43 | 9.572 | 14.25 | 9.578 | 14.41 | 9.595 | 14.5 | 9.606 | 14.36 | 9.672 | 14.55 |
| pods started | 5.714 | 11.29 | 5.229 | 12.4 | 5.4 | 10.97 | 5.4 | 11.4 | 5.171 | 11.17 | 5.114 | 11.57 | 4.943 | 11.43 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 178.3 | 178.6 | 182.1 | 181.4 | 179.5 | 179.7 | 179.3 | 180.1 | 182 | 181.1 | 181.3 | 180.6 | 182.6 | 181.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.3 | 178.6 | 182.1 | 181.4 | 179.5 | 179.7 | 179.3 | 180.1 | 182 | 181.1 | 181.3 | 180.6 | 182.6 | 181.7 |
| CPU used with Omni's own (cores), mean | 1.793 | 1.839 | 2.104 | 2.14 | 1.913 | 1.96 | 1.895 | 1.949 | 2.1 | 2.146 | 2.061 | 2.093 | 2.155 | 2.196 |
| host CPU busy, the real machine under kind (%) | 54.06 | 55.58 | 62.67 | 64.11 | 57.28 | 58.98 | 56.87 | 58.54 | 62.45 | 64.2 | 61.55 | 62.93 | 64.51 | 66.37 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1319 | 1005 | -23.8% | -569.7 to -57.55 | GAIN |
| response time (ms), 99th percentile | 4335 | 3977 | -8.2% | -572.2 to -143 | GAIN |
| time over the response line (% of samples) | 14.17 | 10.54 | -25.6% | -4.792 to -2.461 | GAIN |
| failed requests (%) | 3.966 | 4.063 | +2.4% | -0.206 to +0.3996 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.532 | 13.97 | +46.6% | +3.954 to +4.921 | power given |
| pods started | 5.714 | 11.29 | +97.5% | +5.023 to +6.12 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.267e-16 to +1.615e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.3 | 178.6 | +0.2% | -0.141 to +0.6949 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.3 | 178.6 | +0.2% | -0.141 to +0.6949 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.793 | 1.839 | +2.6% | +0.03538 to +0.0571 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.06 | 55.58 | +2.8% | +1.156 to +1.868 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.981e+05 to +7.991e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.409e-05 to -9.398e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1280 | 1490 | +16.4% | -39.53 to +459.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4951 | 5232 | +5.7% | -183.8 to +747.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 23.31 | 17.98 | -22.8% | -6.887 to -3.759 | GAIN |
| failed requests (%) | 9.553 | 8.423 | -11.8% | -1.865 to -0.3951 | GAIN |
| HPA replicas, mean | 9.641 | 14.43 | +49.7% | +4.499 to +5.082 | power given |
| pods started | 5.229 | 12.4 | +137.2% | +6.704 to +7.639 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.551e-16 to +4.454e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.1 | 181.4 | -0.4% | -1.168 to -0.3256 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.1 | 181.4 | -0.4% | -1.168 to -0.3256 | GAIN |
| CPU used with Omni's own (cores), mean | 2.104 | 2.14 | +1.7% | +0.02536 to +0.0464 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.67 | 64.11 | +2.3% | +1.148 to +1.743 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.621e+05 to +8.625e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.149e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1454 | 1261 | -13.3% | -420.3 to +33.48 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4808 | 4575 | -4.9% | -583.5 to +116.5 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 17.21 | 12.84 | -25.4% | -5.599 to -3.137 | GAIN |
| failed requests (%) | 5.668 | 5.429 | -4.2% | -0.6053 to +0.1277 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.572 | 14.25 | +48.9% | +4.245 to +5.113 | power given |
| pods started | 5.4 | 10.97 | +103.2% | +5.161 to +5.982 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.079e-16 to -1.071e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.5 | 179.7 | +0.1% | -0.1572 to +0.6487 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.5 | 179.7 | +0.1% | -0.1572 to +0.6487 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.913 | 1.96 | +2.4% | +0.03628 to +0.05663 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.28 | 58.98 | +3.0% | +1.408 to +1.987 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1352 | 1089 | -19.4% | -479 to -46.83 | GAIN |
| response time (ms), 99th percentile | 4703 | 4618 | -1.8% | -452.9 to +283.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 15.17 | 11.21 | -26.1% | -5.3 to -2.626 | GAIN |
| failed requests (%) | 4.53 | 4.26 | -6.0% | -0.6757 to +0.1352 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.578 | 14.41 | +50.5% | +4.532 to +5.133 | power given |
| pods started | 5.4 | 11.4 | +111.1% | +5.551 to +6.449 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.426e-16 to +1.858e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.3 | 180.1 | +0.4% | +0.3945 to +1.051 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.3 | 180.1 | +0.4% | +0.3945 to +1.051 | power given |
| CPU used with Omni's own (cores), mean | 1.895 | 1.949 | +2.9% | +0.04294 to +0.06654 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.87 | 58.54 | +2.9% | +1.425 to +1.921 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1508 | 1706 | +13.1% | -65.49 to +459.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4682 | 5089 | +8.7% | -18.13 to +830.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 22.58 | 17.62 | -22.0% | -6.045 to -3.882 | GAIN |
| failed requests (%) | 6.772 | 6.386 | -5.7% | -0.7407 to -0.031 | GAIN |
| HPA replicas, mean | 9.595 | 14.5 | +51.1% | +4.538 to +5.277 | power given |
| pods started | 5.171 | 11.17 | +116.0% | +5.5 to +6.5 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.509e-17 to +5.726e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182 | 181.1 | -0.5% | -1.354 to -0.4998 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182 | 181.1 | -0.5% | -1.354 to -0.4998 | GAIN |
| CPU used with Omni's own (cores), mean | 2.1 | 2.146 | +2.2% | +0.03646 to +0.05525 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.45 | 64.2 | +2.8% | +1.493 to +1.992 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1590 | 1538 | -3.3% | -295.5 to +191.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4882 | 4809 | -1.5% | -601.2 to +455.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 21.92 | 17.68 | -19.3% | -5.834 to -2.63 | GAIN |
| failed requests (%) | 7.929 | 6.504 | -18.0% | -2.305 to -0.544 | GAIN |
| HPA replicas, mean | 9.606 | 14.36 | +49.5% | +4.471 to +5.034 | power given |
| pods started | 5.114 | 11.57 | +126.3% | +5.902 to +7.012 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.136e-16 to +1.538e-18 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.3 | 180.6 | -0.4% | -1.229 to -0.238 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.3 | 180.6 | -0.4% | -1.229 to -0.238 | GAIN |
| CPU used with Omni's own (cores), mean | 2.061 | 2.093 | +1.6% | +0.01877 to +0.04572 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.55 | 62.93 | +2.2% | +0.9863 to +1.779 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1393 | 1742 | +25.0% | +84.49 to +612.2 | LOSS |
| response time (ms), 99th percentile | 4589 | 4954 | +8.0% | -154.1 to +884.3 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 26.19 | 21.76 | -16.9% | -6.579 to -2.269 | GAIN |
| failed requests (%) | 11.2 | 10.34 | -7.7% | -2.058 to +0.3444 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.672 | 14.55 | +50.4% | +4.57 to +5.187 | power given |
| pods started | 4.943 | 11.43 | +131.2% | +5.792 to +7.18 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.436e-16 to -1.473e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.6 | 181.7 | -0.5% | -1.355 to -0.5495 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.6 | 181.7 | -0.5% | -1.355 to -0.5495 | GAIN |
| CPU used with Omni's own (cores), mean | 2.155 | 2.196 | +1.9% | +0.02923 to +0.05312 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.51 | 66.37 | +2.9% | +1.539 to +2.167 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
