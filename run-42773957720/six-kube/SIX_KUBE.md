# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on: native | The spine, the muscles every stack runs on: omni | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1229 | 1338 | 1397 | 1512 | 1448 | 1417 | 1329 | 1292 | 1231 | 1403 |
| response time (ms), 99th percentile | 4191 | 4275 | 4951 | 5291 | 4841 | 4683 | 3855 | 4096 | 4336 | 4886 |
| time over the response line (% of samples) | 13.6 | 10.5 | 23.99 | 18.95 | 16.91 | 12.9 | 19.68 | 15.75 | 20.6 | 15.54 |
| failed requests (%) | 4.202 | 3.784 | 10.06 | 8.896 | 5.302 | 4.99 | 7.118 | 6.235 | 8.315 | 6.895 |
| HPA replicas, mean | 9.543 | 14.1 | 9.67 | 14.58 | 9.576 | 14.07 | 9.555 | 14.18 | 9.644 | 14.04 |
| pods started | 5.604 | 11.62 | 4.958 | 12 | 5.292 | 10.79 | 5.562 | 11.96 | 4.979 | 12.1 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 178.4 | 178.7 | 182.3 | 181.7 | 179.5 | 179.4 | 180.2 | 179.9 | 181.1 | 180.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.4 | 178.7 | 182.3 | 181.7 | 179.5 | 179.4 | 180.2 | 179.9 | 181.1 | 180.3 |
| CPU used with Omni's own (cores), mean | 1.799 | 1.837 | 2.151 | 2.183 | 1.911 | 1.946 | 1.957 | 2.005 | 2.035 | 2.07 |
| host CPU busy, the real machine under kind (%) | 53.94 | 55.49 | 63.74 | 65.2 | 56.9 | 58.31 | 58.39 | 60.09 | 60.75 | 62.33 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.08125 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

48 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1229 | 1338 | +8.9% | -129.8 to +347.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4191 | 4275 | +2.0% | -227.2 to +393.6 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 13.6 | 10.5 | -22.8% | -3.962 to -2.227 | GAIN |
| failed requests (%) | 4.202 | 3.784 | -9.9% | -0.749 to -0.08663 | GAIN |
| HPA replicas, mean | 9.543 | 14.1 | +47.8% | +4.183 to +4.94 | power given |
| pods started | 5.604 | 11.62 | +107.4% | +5.567 to +6.475 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.287e-16 to +3.067e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.4 | 178.7 | +0.2% | -0.009876 to +0.6134 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.4 | 178.7 | +0.2% | -0.009876 to +0.6134 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.799 | 1.837 | +2.1% | +0.02868 to +0.04672 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 53.94 | 55.49 | +2.9% | +1.355 to +1.741 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.983e+05 to +8.005e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.426e-05 to -9.4e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

48 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1397 | 1512 | +8.2% | -94.92 to +325.4 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4951 | 5291 | +6.9% | -121.2 to +801.8 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 23.99 | 18.95 | -21.0% | -6.539 to -3.547 | GAIN |
| failed requests (%) | 10.06 | 8.896 | -11.6% | -1.795 to -0.5287 | GAIN |
| HPA replicas, mean | 9.67 | 14.58 | +50.8% | +4.722 to +5.103 | power given |
| pods started | 4.958 | 12 | +142.0% | +6.503 to +7.581 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.696e-16 to -2.886e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 181.7 | -0.3% | -0.9541 to -0.2134 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 181.7 | -0.3% | -0.9541 to -0.2134 | GAIN |
| CPU used with Omni's own (cores), mean | 2.151 | 2.183 | +1.5% | +0.02087 to +0.04381 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.74 | 65.2 | +2.3% | +1.169 to +1.75 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.621e+05 to +8.625e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.15e-05 to -8.145e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

48 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1448 | 1417 | -2.1% | -229 to +167.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4841 | 4683 | -3.3% | -464 to +148.3 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.91 | 12.9 | -23.7% | -5.117 to -2.897 | GAIN |
| failed requests (%) | 5.302 | 4.99 | -5.9% | -0.7338 to +0.1083 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.576 | 14.07 | +46.9% | +4.065 to +4.919 | power given |
| pods started | 5.292 | 10.79 | +103.9% | +4.904 to +6.096 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.605e-16 to +2.975e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.5 | 179.4 | -0.0% | -0.4787 to +0.3547 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.5 | 179.4 | -0.0% | -0.4787 to +0.3547 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.911 | 1.946 | +1.8% | +0.02085 to +0.04915 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.9 | 58.31 | +2.5% | +1.009 to +1.804 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

48 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1329 | 1292 | -2.8% | -191.9 to +117 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3855 | 4096 | +6.3% | -90.96 to +573.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 19.68 | 15.75 | -20.0% | -5.223 to -2.637 | GAIN |
| failed requests (%) | 7.118 | 6.235 | -12.4% | -1.601 to -0.1645 | GAIN |
| HPA replicas, mean | 9.555 | 14.18 | +48.4% | +4.345 to +4.896 | power given |
| pods started | 5.562 | 11.96 | +115.0% | +6.004 to +6.787 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.902e-16 to +1.351e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.2 | 179.9 | -0.2% | -0.6592 to +0.06289 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.2 | 179.9 | -0.2% | -0.6592 to +0.06289 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.957 | 2.005 | +2.4% | +0.03724 to +0.0582 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.39 | 60.09 | +2.9% | +1.405 to +2.006 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 0

48 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1231 | 1403 | +13.9% | +1.751 to +340.5 | LOSS |
| response time (ms), 99th percentile | 4336 | 4886 | +12.7% | +121.4 to +978.5 | LOSS |
| time over the response line (% of samples) | 20.6 | 15.54 | -24.5% | -6.494 to -3.617 | GAIN |
| failed requests (%) | 8.315 | 6.895 | -17.1% | -2.058 to -0.781 | GAIN |
| HPA replicas, mean | 9.644 | 14.04 | +45.5% | +4.103 to +4.681 | power given |
| pods started | 4.979 | 12.1 | +143.1% | +6.625 to +7.625 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.459e-16 to +1.498e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 180.3 | -0.4% | -1.182 to -0.4248 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 180.3 | -0.4% | -1.182 to -0.4248 | GAIN |
| CPU used with Omni's own (cores), mean | 2.035 | 2.07 | +1.7% | +0.0245 to +0.04594 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.75 | 62.33 | +2.6% | +1.278 to +1.866 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.08125 | +0.0813 | +0.0698 to +0.0927 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Energy / Facility / Industrial
- Distribution / Specialized

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
