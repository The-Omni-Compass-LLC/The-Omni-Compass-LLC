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
| response time (ms), 95th percentile | 1564 | 1492 | 1273 | 1324 | 1706 | 1545 | 1519 | 1353 | 1502 | 1433 | 1940 | 2136 | 1243 | 1370 |
| response time (ms), 99th percentile | 5192 | 5004 | 4323 | 4682 | 5543 | 5633 | 4868 | 4573 | 4661 | 4528 | 5187 | 5558 | 4491 | 4765 |
| time over the response line (% of samples) | 18.25 | 13.73 | 20.61 | 16.58 | 18.47 | 14.32 | 16.77 | 12.97 | 22.14 | 17.49 | 28.17 | 23.69 | 21.61 | 17.34 |
| failed requests (%) | 6.016 | 5.777 | 8.494 | 7.76 | 6.006 | 5.668 | 5.405 | 5.133 | 6.601 | 6.536 | 10.9 | 9.979 | 9.142 | 7.759 |
| HPA replicas, mean | 9.595 | 14.48 | 9.636 | 14.23 | 9.618 | 14.47 | 9.587 | 14.26 | 9.584 | 14.49 | 9.643 | 14.66 | 9.638 | 14.18 |
| pods started | 5.286 | 11.23 | 5.114 | 12.46 | 5.029 | 11.09 | 5.2 | 11.43 | 5.2 | 11.17 | 4.829 | 11.11 | 5.314 | 12.2 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.7 | 179.9 | 181 | 180.6 | 180.1 | 180.5 | 179.4 | 179.8 | 181.7 | 181 | 182.7 | 182.2 | 181.7 | 181 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.7 | 179.9 | 181 | 180.6 | 180.1 | 180.5 | 179.4 | 179.8 | 181.7 | 181 | 182.7 | 182.2 | 181.7 | 181 |
| CPU used with Omni's own (cores), mean | 1.941 | 1.991 | 2.014 | 2.054 | 1.983 | 2.042 | 1.913 | 1.953 | 2.074 | 2.121 | 2.185 | 2.233 | 2.075 | 2.11 |
| host CPU busy, the real machine under kind (%) | 58.07 | 59.69 | 60.26 | 61.8 | 59.34 | 61.16 | 57.21 | 58.84 | 61.8 | 63.67 | 64.93 | 66.79 | 62.14 | 63.7 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1564 | 1492 | -4.6% | -364 to +220.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5192 | 5004 | -3.6% | -622.8 to +247.5 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 18.25 | 13.73 | -24.8% | -5.929 to -3.106 | GAIN |
| failed requests (%) | 6.016 | 5.777 | -4.0% | -1.104 to +0.6263 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.595 | 14.48 | +50.9% | +4.586 to +5.178 | power given |
| pods started | 5.286 | 11.23 | +112.4% | +5.391 to +6.495 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.884e-16 to +4.914e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.7 | 179.9 | +0.1% | -0.2107 to +0.6911 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.7 | 179.9 | +0.1% | -0.2107 to +0.6911 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.941 | 1.991 | +2.6% | +0.03358 to +0.06594 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.07 | 59.69 | +2.8% | +1.229 to +2.013 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.981e+05 to +7.996e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.415e-05 to -9.398e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1273 | 1324 | +4.1% | -166 to +269.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4323 | 4682 | +8.3% | -202.1 to +921 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 20.61 | 16.58 | -19.5% | -5.866 to -2.186 | GAIN |
| failed requests (%) | 8.494 | 7.76 | -8.6% | -1.63 to +0.1622 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.636 | 14.23 | +47.6% | +4.267 to +4.914 | power given |
| pods started | 5.114 | 12.46 | +143.6% | +6.823 to +7.863 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.053e-16 to +9.775e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180.6 | -0.2% | -0.7876 to +0.04339 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180.6 | -0.2% | -0.7876 to +0.04339 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.014 | 2.054 | +2.0% | +0.02407 to +0.05517 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.26 | 61.8 | +2.6% | +1.1 to +1.974 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.621e+05 to +8.627e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.151e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1706 | 1545 | -9.4% | -484.4 to +162.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5543 | 5633 | +1.6% | -327.9 to +507.9 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 18.47 | 14.32 | -22.5% | -5.114 to -3.187 | GAIN |
| failed requests (%) | 6.006 | 5.668 | -5.6% | -0.7024 to +0.02558 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.618 | 14.47 | +50.5% | +4.533 to +5.178 | power given |
| pods started | 5.029 | 11.09 | +120.5% | +5.457 to +6.658 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.141e-16 to +2.588e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.1 | 180.5 | +0.2% | -0.07462 to +0.7943 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.1 | 180.5 | +0.2% | -0.07462 to +0.7943 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.983 | 2.042 | +3.0% | +0.05013 to +0.06743 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.34 | 61.16 | +3.1% | +1.548 to +2.092 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1519 | 1353 | -11.0% | -458 to +125.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4868 | 4573 | -6.1% | -779.6 to +188.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.77 | 12.97 | -22.6% | -4.976 to -2.618 | GAIN |
| failed requests (%) | 5.405 | 5.133 | -5.0% | -0.7013 to +0.1572 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.587 | 14.26 | +48.7% | +4.271 to +5.066 | power given |
| pods started | 5.2 | 11.43 | +119.8% | +5.663 to +6.794 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.962e-16 to +1.379e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.4 | 179.8 | +0.2% | -0.101 to +0.8069 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.4 | 179.8 | +0.2% | -0.101 to +0.8069 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.913 | 1.953 | +2.1% | +0.02786 to +0.05122 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.21 | 58.84 | +2.9% | +1.35 to +1.911 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1502 | 1433 | -4.6% | -232.8 to +95.52 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4661 | 4528 | -2.9% | -608.6 to +342.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 22.14 | 17.49 | -21.0% | -5.908 to -3.38 | GAIN |
| failed requests (%) | 6.601 | 6.536 | -1.0% | -0.3578 to +0.229 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.584 | 14.49 | +51.2% | +4.548 to +5.271 | power given |
| pods started | 5.2 | 11.17 | +114.8% | +5.38 to +6.563 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.75e-16 to +2.213e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.7 | 181 | -0.4% | -1.208 to -0.3384 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.7 | 181 | -0.4% | -1.208 to -0.3384 | GAIN |
| CPU used with Omni's own (cores), mean | 2.074 | 2.121 | +2.2% | +0.03467 to +0.05802 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.8 | 63.67 | +3.0% | +1.571 to +2.172 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1940 | 2136 | +10.1% | -83.41 to +475.4 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5187 | 5558 | +7.2% | -60 to +802.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 28.17 | 23.69 | -15.9% | -5.755 to -3.193 | GAIN |
| failed requests (%) | 10.9 | 9.979 | -8.5% | -1.417 to -0.4316 | GAIN |
| HPA replicas, mean | 9.643 | 14.66 | +52.1% | +4.813 to +5.23 | power given |
| pods started | 4.829 | 11.11 | +130.2% | +5.762 to +6.81 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.804e-16 to +2.759e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.7 | 182.2 | -0.3% | -0.928 to -0.1372 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.7 | 182.2 | -0.3% | -0.928 to -0.1372 | GAIN |
| CPU used with Omni's own (cores), mean | 2.185 | 2.233 | +2.2% | +0.04066 to +0.05651 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.93 | 66.79 | +2.9% | +1.661 to +2.044 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1243 | 1370 | +10.2% | -58.33 to +311.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4491 | 4765 | +6.1% | -268.4 to +817.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 21.61 | 17.34 | -19.8% | -6.267 to -2.27 | GAIN |
| failed requests (%) | 9.142 | 7.759 | -15.1% | -2.334 to -0.4313 | GAIN |
| HPA replicas, mean | 9.638 | 14.18 | +47.2% | +4.194 to +4.896 | power given |
| pods started | 5.314 | 12.2 | +129.6% | +6.381 to +7.391 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.349e-16 to +2.59e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.7 | 181 | -0.4% | -1.244 to -0.2778 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.7 | 181 | -0.4% | -1.244 to -0.2778 | GAIN |
| CPU used with Omni's own (cores), mean | 2.075 | 2.11 | +1.7% | +0.02118 to +0.04826 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.14 | 63.7 | +2.5% | +1.157 to +1.955 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
