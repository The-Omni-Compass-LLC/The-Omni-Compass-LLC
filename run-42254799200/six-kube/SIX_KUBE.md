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
| response time (ms), 95th percentile | 1886 | 1561 | 1356 | 1281 | 1154 | 972.4 | 1300 | 1099 | 1552 | 1519 | 1041 | 1092 |
| response time (ms), 99th percentile | 5969 | 5546 | 4332 | 4536 | 3766 | 3604 | 4596 | 4296 | 4418 | 4441 | 3729 | 4124 |
| time over the response line (% of samples) | 20.32 | 16.1 | 22.7 | 16.09 | 12.89 | 9.514 | 14.17 | 10.62 | 21.79 | 17.73 | 16.14 | 12.63 |
| failed requests (%) | 6.584 | 6.531 | 9.536 | 7.723 | 3.897 | 3.794 | 4.138 | 3.965 | 7.929 | 7.244 | 6.429 | 5.479 |
| HPA replicas, mean | 9.631 | 14.68 | 9.636 | 14.22 | 9.515 | 14.06 | 9.56 | 14.18 | 9.588 | 14.22 | 9.565 | 14.03 |
| pods started | 4.902 | 10.95 | 4.951 | 11.9 | 5.659 | 11.56 | 5.463 | 11.32 | 5.244 | 11.9 | 5.878 | 12.88 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 181 | 181.1 | 180.1 | 178 | 178.5 | 178.8 | 179.4 | 181.1 | 180.5 | 179.9 | 179.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 181 | 181.1 | 180.1 | 178 | 178.5 | 178.8 | 179.4 | 181.1 | 180.5 | 179.9 | 179.2 |
| CPU used with Omni's own (cores), mean | 2.041 | 2.092 | 2.012 | 2.041 | 1.759 | 1.811 | 1.84 | 1.881 | 2.022 | 2.064 | 1.899 | 1.924 |
| host CPU busy, the real machine under kind (%) | 60.49 | 62.34 | 59.92 | 61.24 | 52.91 | 54.43 | 55.15 | 56.51 | 60.16 | 61.77 | 56.76 | 58.15 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.09268 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1886 | 1561 | -17.2% | -619.4 to -30.5 | GAIN |
| response time (ms), 99th percentile | 5969 | 5546 | -7.1% | -808.3 to -37.21 | GAIN |
| time over the response line (% of samples) | 20.32 | 16.1 | -20.8% | -5.009 to -3.433 | GAIN |
| failed requests (%) | 6.584 | 6.531 | -0.8% | -0.3577 to +0.2524 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.631 | 14.68 | +52.5% | +4.861 to +5.243 | power given |
| pods started | 4.902 | 10.95 | +123.4% | +5.493 to +6.604 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.003e-16 to +1.537e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 181 | +0.2% | -0.07496 to +0.7986 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 181 | +0.2% | -0.07496 to +0.7986 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.041 | 2.092 | +2.5% | +0.03887 to +0.06417 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.49 | 62.34 | +3.0% | +1.573 to +2.11 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.985e+05 to +8.007e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.428e-05 to -9.402e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1356 | 1281 | -5.5% | -336.4 to +186.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4332 | 4536 | +4.7% | -308.8 to +718.3 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 22.7 | 16.09 | -29.1% | -8.709 to -4.515 | GAIN |
| failed requests (%) | 9.536 | 7.723 | -19.0% | -2.798 to -0.8275 | GAIN |
| HPA replicas, mean | 9.636 | 14.22 | +47.6% | +4.365 to +4.805 | power given |
| pods started | 4.951 | 11.9 | +140.4% | +6.505 to +7.397 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.826e-16 to +7.6e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 180.1 | -0.6% | -1.496 to -0.5997 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 180.1 | -0.6% | -1.496 to -0.5997 | GAIN |
| CPU used with Omni's own (cores), mean | 2.012 | 2.041 | +1.5% | +0.01717 to +0.04143 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.92 | 61.24 | +2.2% | +1.05 to +1.606 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.62e+05 to +8.624e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.149e-05 to -8.144e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1154 | 972.4 | -15.8% | -435.9 to +72.04 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3766 | 3604 | -4.3% | -512.7 to +188.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 12.89 | 9.514 | -26.2% | -4.437 to -2.317 | GAIN |
| failed requests (%) | 3.897 | 3.794 | -2.7% | -0.3465 to +0.1391 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.515 | 14.06 | +47.8% | +4.171 to +4.921 | power given |
| pods started | 5.659 | 11.56 | +104.3% | +5.441 to +6.364 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.755e-16 to +1.423e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178 | 178.5 | +0.3% | +0.1835 to +0.7641 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178 | 178.5 | +0.3% | +0.1835 to +0.7641 | power given |
| CPU used with Omni's own (cores), mean | 1.759 | 1.811 | +3.0% | +0.04339 to +0.06093 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 52.91 | 54.43 | +2.9% | +1.255 to +1.789 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1300 | 1099 | -15.4% | -435.2 to +34.64 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4596 | 4296 | -6.5% | -544.8 to -54.91 | GAIN |
| time over the response line (% of samples) | 14.17 | 10.62 | -25.1% | -4.386 to -2.719 | GAIN |
| failed requests (%) | 4.138 | 3.965 | -4.2% | -0.4356 to +0.09018 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.56 | 14.18 | +48.3% | +4.244 to +4.992 | power given |
| pods started | 5.463 | 11.32 | +107.1% | +5.309 to +6.398 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.877e-16 to +2.277e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.8 | 179.4 | +0.3% | +0.2216 to +0.9708 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.8 | 179.4 | +0.3% | +0.2216 to +0.9708 | power given |
| CPU used with Omni's own (cores), mean | 1.84 | 1.881 | +2.2% | +0.02811 to +0.05344 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.15 | 56.51 | +2.5% | +1.082 to +1.636 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1552 | 1519 | -2.1% | -205 to +138.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4418 | 4441 | +0.5% | -366.6 to +413.3 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 21.79 | 17.73 | -18.6% | -5.473 to -2.644 | GAIN |
| failed requests (%) | 7.929 | 7.244 | -8.6% | -1.325 to -0.04597 | GAIN |
| HPA replicas, mean | 9.588 | 14.22 | +48.3% | +4.304 to +4.954 | power given |
| pods started | 5.244 | 11.9 | +127.0% | +6.198 to +7.119 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.103e-16 to +9.043e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 180.5 | -0.3% | -0.9624 to -0.2177 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 180.5 | -0.3% | -0.9624 to -0.2177 | GAIN |
| CPU used with Omni's own (cores), mean | 2.022 | 2.064 | +2.1% | +0.03042 to +0.05338 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.16 | 61.77 | +2.7% | +1.254 to +1.965 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1041 | 1092 | +5.0% | -82.5 to +185.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3729 | 4124 | +10.6% | -27.57 to +816.9 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 16.14 | 12.63 | -21.7% | -4.833 to -2.183 | GAIN |
| failed requests (%) | 6.429 | 5.479 | -14.8% | -1.583 to -0.3181 | GAIN |
| HPA replicas, mean | 9.565 | 14.03 | +46.7% | +4.119 to +4.805 | power given |
| pods started | 5.878 | 12.88 | +119.1% | +6.397 to +7.603 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.529e-16 to +1.197e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.9 | 179.2 | -0.4% | -1.189 to -0.3791 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.9 | 179.2 | -0.4% | -1.189 to -0.3791 | GAIN |
| CPU used with Omni's own (cores), mean | 1.899 | 1.924 | +1.3% | +0.007352 to +0.04286 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.76 | 58.15 | +2.4% | +0.993 to +1.783 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.09268 | +0.0927 | +0.08177 to +0.1036 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Distribution / Specialized

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
