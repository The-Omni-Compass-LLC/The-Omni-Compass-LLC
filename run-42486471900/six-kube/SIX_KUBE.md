# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on: native | The spine, the muscles every stack runs on: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1547 | 1235 | 1475 | 1247 | 1415 | 1387 | 1505 | 1470 | 1448 | 1591 |
| response time (ms), 99th percentile | 4269 | 4090 | 4725 | 4540 | 4040 | 4360 | 4782 | 4807 | 4911 | 4995 |
| time over the response line (% of samples) | 14.61 | 11.19 | 16.76 | 12.66 | 18.9 | 14.98 | 20.37 | 16.72 | 25.02 | 19.26 |
| failed requests (%) | 4.374 | 4.508 | 5.562 | 5.209 | 5.818 | 5.74 | 6.792 | 6.622 | 10.6 | 9.306 |
| HPA replicas, mean | 9.56 | 13.99 | 9.595 | 14.51 | 9.537 | 13.56 | 9.589 | 14.52 | 9.627 | 14.38 |
| pods started | 5.4 | 12.15 | 5.1 | 11.2 | 5.45 | 11.05 | 5.05 | 10.9 | 5.3 | 11.8 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 178.3 | 178.7 | 179.8 | 180.2 | 180.2 | 179.6 | 181.2 | 180.4 | 181.8 | 181.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.3 | 178.7 | 179.8 | 180.2 | 180.2 | 179.6 | 181.2 | 180.4 | 181.8 | 181.3 |
| CPU used with Omni's own (cores), mean | 1.806 | 1.858 | 1.945 | 1.991 | 1.929 | 1.967 | 2.018 | 2.063 | 2.102 | 2.144 |
| host CPU busy, the real machine under kind (%) | 54.09 | 55.79 | 57.95 | 59.75 | 57.61 | 59.02 | 60.02 | 61.69 | 62.57 | 64.33 |
| organism work | 2.05e+10 | 2.05e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.09 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1547 | 1235 | -20.1% | -693.5 to +70.89 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4269 | 4090 | -4.2% | -824.4 to +466.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 14.61 | 11.19 | -23.4% | -4.851 to -1.975 | GAIN |
| failed requests (%) | 4.374 | 4.508 | +3.1% | -0.269 to +0.5377 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.56 | 13.99 | +46.4% | +3.81 to +5.052 | power given |
| pods started | 5.4 | 12.15 | +125.0% | +6.108 to +7.392 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.881e-16 to +7.434e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.3 | 178.7 | +0.2% | -0.1796 to +0.9808 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.3 | 178.7 | +0.2% | -0.1796 to +0.9808 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.806 | 1.858 | +2.9% | +0.03779 to +0.06564 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.09 | 55.79 | +3.1% | +1.34 to +2.046 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.982e+05 to +8.021e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.445e-05 to -9.4e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1475 | 1247 | -15.5% | -727.1 to +271 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4725 | 4540 | -3.9% | -821.5 to +451.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.76 | 12.66 | -24.5% | -5.546 to -2.663 | GAIN |
| failed requests (%) | 5.562 | 5.209 | -6.3% | -0.9053 to +0.1991 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.595 | 14.51 | +51.3% | +4.546 to +5.289 | power given |
| pods started | 5.1 | 11.2 | +119.6% | +5.622 to +6.578 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.493e-16 to +2.387e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 180.2 | +0.2% | -0.2153 to +1.039 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 180.2 | +0.2% | -0.2153 to +1.039 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.945 | 1.991 | +2.4% | +0.0307 to +0.06148 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.95 | 59.75 | +3.1% | +1.526 to +2.084 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1415 | 1387 | -2.0% | -232.5 to +176.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4040 | 4360 | +7.9% | -335.5 to +975.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 18.9 | 14.98 | -20.7% | -5.963 to -1.876 | GAIN |
| failed requests (%) | 5.818 | 5.74 | -1.3% | -0.6471 to +0.4911 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.537 | 13.56 | +42.1% | +3.163 to +4.875 | power given |
| pods started | 5.45 | 11.05 | +102.8% | +4.49 to +6.71 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.241e-15 to -2.236e-18 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.2 | 179.6 | -0.3% | -1.125 to -0.07727 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.2 | 179.6 | -0.3% | -1.125 to -0.07727 | GAIN |
| CPU used with Omni's own (cores), mean | 1.929 | 1.967 | +2.0% | +0.02132 to +0.0541 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.61 | 59.02 | +2.4% | +0.9478 to +1.866 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1505 | 1470 | -2.3% | -354.4 to +283.8 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4782 | 4807 | +0.5% | -603.9 to +653.8 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 20.37 | 16.72 | -17.9% | -5.04 to -2.262 | GAIN |
| failed requests (%) | 6.792 | 6.622 | -2.5% | -0.8755 to +0.5357 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.589 | 14.52 | +51.5% | +4.63 to +5.237 | power given |
| pods started | 5.05 | 10.9 | +115.8% | +5.166 to +6.534 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.069e-15 to -8.594e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.2 | 180.4 | -0.4% | -1.363 to -0.1291 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.2 | 180.4 | -0.4% | -1.363 to -0.1291 | GAIN |
| CPU used with Omni's own (cores), mean | 2.018 | 2.063 | +2.2% | +0.0313 to +0.05813 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.02 | 61.69 | +2.8% | +1.303 to +2.043 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1448 | 1591 | +9.8% | -197.7 to +482.8 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4911 | 4995 | +1.7% | -507.4 to +676 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 25.02 | 19.26 | -23.0% | -8.256 to -3.274 | GAIN |
| failed requests (%) | 10.6 | 9.306 | -12.3% | -2.371 to -0.2273 | GAIN |
| HPA replicas, mean | 9.627 | 14.38 | +49.4% | +4.383 to +5.129 | power given |
| pods started | 5.3 | 11.8 | +122.6% | +5.4 to +7.6 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.199e-15 to +4.474e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.8 | 181.3 | -0.3% | -1.107 to +0.1075 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.8 | 181.3 | -0.3% | -1.107 to +0.1075 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.102 | 2.144 | +2.0% | +0.02554 to +0.05738 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.57 | 64.33 | +2.8% | +1.334 to +2.193 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.09 | +0.09 | +0.07559 to +0.1044 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
