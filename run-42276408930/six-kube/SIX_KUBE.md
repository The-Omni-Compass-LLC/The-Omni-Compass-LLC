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
| response time (ms), 95th percentile | 1779 | 1483 | 1313 | 1302 | 1710 | 1570 | 1276 | 1128 | 1973 | 2270 | 1304 | 1220 |
| response time (ms), 99th percentile | 5846 | 5357 | 4725 | 4828 | 5264 | 5397 | 3884 | 3833 | 5266 | 5483 | 4874 | 4948 |
| time over the response line (% of samples) | 20.32 | 14.93 | 20.2 | 16.3 | 18.52 | 14.15 | 13.25 | 10.01 | 31.02 | 25.81 | 20.44 | 15.65 |
| failed requests (%) | 6.47 | 6.161 | 8.278 | 7.607 | 5.812 | 5.505 | 3.949 | 3.874 | 12.3 | 11.64 | 7.961 | 7.142 |
| HPA replicas, mean | 9.639 | 14.66 | 9.63 | 14.35 | 9.604 | 14.15 | 9.535 | 13.88 | 9.665 | 14.57 | 9.62 | 14.31 |
| pods started | 4.878 | 11 | 5.244 | 12.22 | 5.098 | 11.05 | 5.659 | 11.2 | 4.439 | 10.39 | 5.39 | 12.12 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 181.3 | 181.2 | 180.6 | 180 | 180.2 | 178.1 | 178.3 | 183.1 | 182.4 | 181.2 | 180.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 181.3 | 181.2 | 180.6 | 180 | 180.2 | 178.1 | 178.3 | 183.1 | 182.4 | 181.2 | 180.4 |
| CPU used with Omni's own (cores), mean | 2.039 | 2.086 | 2.037 | 2.079 | 1.978 | 2.02 | 1.771 | 1.812 | 2.21 | 2.262 | 2.027 | 2.063 |
| host CPU busy, the real machine under kind (%) | 60.58 | 62.14 | 60.64 | 62.35 | 58.76 | 60.32 | 53.14 | 54.6 | 65.35 | 67.27 | 60.42 | 62.04 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.07317 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1779 | 1483 | -16.6% | -566 to -25.24 | GAIN |
| response time (ms), 99th percentile | 5846 | 5357 | -8.4% | -839.4 to -137.6 | GAIN |
| time over the response line (% of samples) | 20.32 | 14.93 | -26.5% | -6.443 to -4.326 | GAIN |
| failed requests (%) | 6.47 | 6.161 | -4.8% | -0.6738 to +0.05617 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.639 | 14.66 | +52.1% | +4.77 to +5.273 | power given |
| pods started | 4.878 | 11 | +125.5% | +5.574 to +6.67 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.172e-16 to +2.439e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 181.3 | +0.3% | +0.1868 to +1.028 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 181.3 | +0.3% | +0.1868 to +1.028 | power given |
| CPU used with Omni's own (cores), mean | 2.039 | 2.086 | +2.3% | +0.03948 to +0.05585 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.58 | 62.14 | +2.6% | +1.344 to +1.777 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.975e+05 to +7.997e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.416e-05 to -9.391e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1313 | 1302 | -0.8% | -224.2 to +202.6 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4725 | 4828 | +2.2% | -422.3 to +626.8 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 20.2 | 16.3 | -19.3% | -5.034 to -2.761 | GAIN |
| failed requests (%) | 8.278 | 7.607 | -8.1% | -1.265 to -0.07796 | GAIN |
| HPA replicas, mean | 9.63 | 14.35 | +49.0% | +4.445 to +5.001 | power given |
| pods started | 5.244 | 12.22 | +133.0% | +6.543 to +7.408 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.326e-16 to +3.026e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.2 | 180.6 | -0.3% | -1.004 to -0.2088 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.2 | 180.6 | -0.3% | -1.004 to -0.2088 | GAIN |
| CPU used with Omni's own (cores), mean | 2.037 | 2.079 | +2.1% | +0.02964 to +0.05438 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.64 | 62.35 | +2.8% | +1.377 to +2.027 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.622e+05 to +8.626e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.151e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1710 | 1570 | -8.2% | -339.9 to +59.77 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5264 | 5397 | +2.5% | -239.2 to +504.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 18.52 | 14.15 | -23.6% | -5.408 to -3.328 | GAIN |
| failed requests (%) | 5.812 | 5.505 | -5.3% | -0.6311 to +0.01685 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.604 | 14.15 | +47.4% | +4.12 to +4.978 | power given |
| pods started | 5.098 | 11.05 | +116.7% | +5.405 to +6.498 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.49e-16 to +5.09e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180 | 180.2 | +0.1% | -0.3164 to +0.5604 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180 | 180.2 | +0.1% | -0.3164 to +0.5604 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.978 | 2.02 | +2.2% | +0.03113 to +0.05455 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.76 | 60.32 | +2.7% | +1.252 to +1.863 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1276 | 1128 | -11.6% | -322 to +25.02 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3884 | 3833 | -1.3% | -324.7 to +222.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 13.25 | 10.01 | -24.5% | -4.236 to -2.252 | GAIN |
| failed requests (%) | 3.949 | 3.874 | -1.9% | -0.2749 to +0.1255 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.535 | 13.88 | +45.6% | +3.86 to +4.827 | power given |
| pods started | 5.659 | 11.2 | +97.8% | +5.063 to +6.011 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.352e-16 to +2.186e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.1 | 178.3 | +0.1% | -0.1264 to +0.6447 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.1 | 178.3 | +0.1% | -0.1264 to +0.6447 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.771 | 1.812 | +2.3% | +0.02881 to +0.05284 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 53.14 | 54.6 | +2.7% | +1.199 to +1.703 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1973 | 2270 | +15.1% | +57.79 to +537.5 | LOSS |
| response time (ms), 99th percentile | 5266 | 5483 | +4.1% | -254.6 to +689.3 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 31.02 | 25.81 | -16.8% | -7.01 to -3.425 | GAIN |
| failed requests (%) | 12.3 | 11.64 | -5.4% | -1.625 to +0.289 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.665 | 14.57 | +50.8% | +4.626 to +5.192 | power given |
| pods started | 4.439 | 10.39 | +134.1% | +5.396 to +6.507 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.72e-16 to +2.388e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.1 | 182.4 | -0.4% | -1.069 to -0.337 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.1 | 182.4 | -0.4% | -1.069 to -0.337 | GAIN |
| CPU used with Omni's own (cores), mean | 2.21 | 2.262 | +2.3% | +0.04147 to +0.06223 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.35 | 67.27 | +2.9% | +1.685 to +2.168 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1304 | 1220 | -6.4% | -221.8 to +54.52 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4874 | 4948 | +1.5% | -388.1 to +536.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 20.44 | 15.65 | -23.4% | -6.193 to -3.392 | GAIN |
| failed requests (%) | 7.961 | 7.142 | -10.3% | -1.347 to -0.2911 | GAIN |
| HPA replicas, mean | 9.62 | 14.31 | +48.8% | +4.374 to +5.006 | power given |
| pods started | 5.39 | 12.12 | +124.9% | +6.238 to +7.226 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.571e-16 to +6.386e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.2 | 180.4 | -0.5% | -1.247 to -0.4285 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.2 | 180.4 | -0.5% | -1.247 to -0.4285 | GAIN |
| CPU used with Omni's own (cores), mean | 2.027 | 2.063 | +1.8% | +0.0255 to +0.04603 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.42 | 62.04 | +2.7% | +1.347 to +1.895 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.07317 | +0.0732 | +0.05901 to +0.08733 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Distribution / Specialized

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
