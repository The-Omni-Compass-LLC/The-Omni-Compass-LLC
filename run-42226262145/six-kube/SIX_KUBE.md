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
| response time (ms), 95th percentile | 1772 | 1581 | 1296 | 1451 | 1575 | 1398 | 1097 | 967.7 | 1076 | 1123 | 1245 | 1217 |
| response time (ms), 99th percentile | 5445 | 5354 | 4547 | 4754 | 5340 | 5232 | 3688 | 3488 | 3387 | 3383 | 4033 | 4249 |
| time over the response line (% of samples) | 19.16 | 15.33 | 22.64 | 17.68 | 16.94 | 13.07 | 13.47 | 9.859 | 14.97 | 11.78 | 20.19 | 15.18 |
| failed requests (%) | 6.599 | 6.438 | 9.278 | 8.376 | 4.716 | 4.525 | 4.35 | 4.108 | 5.187 | 4.256 | 8.194 | 6.856 |
| HPA replicas, mean | 9.624 | 14.75 | 9.652 | 14.4 | 9.609 | 14.54 | 9.524 | 13.68 | 9.506 | 13.97 | 9.595 | 14.13 |
| pods started | 5.024 | 10.93 | 5 | 11.71 | 5.22 | 11.1 | 5.561 | 11.61 | 5.902 | 12.56 | 5.537 | 12.54 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180.5 | 180.8 | 181.4 | 180.9 | 180.2 | 180.7 | 177.6 | 178.2 | 179 | 178.6 | 180.5 | 180 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.5 | 180.8 | 181.4 | 180.9 | 180.2 | 180.7 | 177.6 | 178.2 | 179 | 178.6 | 180.5 | 180 |
| CPU used with Omni's own (cores), mean | 2.025 | 2.076 | 2.073 | 2.115 | 1.977 | 2.027 | 1.739 | 1.782 | 1.823 | 1.86 | 1.979 | 2.008 |
| host CPU busy, the real machine under kind (%) | 60.31 | 61.99 | 61.66 | 63.18 | 58.88 | 60.56 | 52.13 | 53.63 | 54.78 | 56.09 | 59.25 | 60.63 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.09024 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1772 | 1581 | -10.8% | -490.9 to +108.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5445 | 5354 | -1.7% | -438.4 to +257.9 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 19.16 | 15.33 | -20.0% | -4.632 to -3.028 | GAIN |
| failed requests (%) | 6.599 | 6.438 | -2.4% | -0.4681 to +0.1463 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.624 | 14.75 | +53.2% | +4.989 to +5.254 | power given |
| pods started | 5.024 | 10.93 | +117.5% | +5.446 to +6.359 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.875e-16 to -2.39e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.5 | 180.8 | +0.2% | -0.1006 to +0.803 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.5 | 180.8 | +0.2% | -0.1006 to +0.803 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.025 | 2.076 | +2.5% | +0.04191 to +0.05946 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.31 | 61.99 | +2.8% | +1.52 to +1.847 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.982e+05 to +7.997e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.417e-05 to -9.399e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1296 | 1451 | +12.0% | -55.82 to +365.8 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4547 | 4754 | +4.6% | -225.7 to +640 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 22.64 | 17.68 | -21.9% | -6.281 to -3.64 | GAIN |
| failed requests (%) | 9.278 | 8.376 | -9.7% | -1.427 to -0.3761 | GAIN |
| HPA replicas, mean | 9.652 | 14.4 | +49.2% | +4.458 to +5.046 | power given |
| pods started | 5 | 11.71 | +134.1% | +6.197 to +7.217 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.721e-16 to +2.988e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 180.9 | -0.2% | -0.893 to -0.005669 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 180.9 | -0.2% | -0.893 to -0.005669 | GAIN |
| CPU used with Omni's own (cores), mean | 2.073 | 2.115 | +2.0% | +0.0306 to +0.05286 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.66 | 63.18 | +2.5% | +1.213 to +1.827 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.623e+05 to +8.627e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.151e-05 to -8.147e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1575 | 1398 | -11.2% | -443.2 to +90.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5340 | 5232 | -2.0% | -555.6 to +340.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.94 | 13.07 | -22.8% | -4.659 to -3.079 | GAIN |
| failed requests (%) | 4.716 | 4.525 | -4.0% | -0.4645 to +0.08291 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.609 | 14.54 | +51.3% | +4.666 to +5.199 | power given |
| pods started | 5.22 | 11.1 | +112.6% | +5.453 to +6.303 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.87e-16 to +2.57e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.2 | 180.7 | +0.3% | +0.09403 to +0.9326 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.2 | 180.7 | +0.3% | +0.09403 to +0.9326 | power given |
| CPU used with Omni's own (cores), mean | 1.977 | 2.027 | +2.5% | +0.04109 to +0.0589 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.88 | 60.56 | +2.8% | +1.474 to +1.871 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1097 | 967.7 | -11.8% | -308.2 to +48.64 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3688 | 3488 | -5.4% | -546.5 to +146.3 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 13.47 | 9.859 | -26.8% | -4.866 to -2.362 | GAIN |
| failed requests (%) | 4.35 | 4.108 | -5.6% | -0.4991 to +0.01521 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.524 | 13.68 | +43.7% | +3.685 to +4.634 | power given |
| pods started | 5.561 | 11.61 | +108.8% | +5.597 to +6.5 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.053e-16 to +1.154e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 177.6 | 178.2 | +0.3% | +0.2762 to +0.9429 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.6 | 178.2 | +0.3% | +0.2762 to +0.9429 | power given |
| CPU used with Omni's own (cores), mean | 1.739 | 1.782 | +2.5% | +0.03468 to +0.0507 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 52.13 | 53.63 | +2.9% | +1.265 to +1.726 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1076 | 1123 | +4.4% | -127.6 to +222.6 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3387 | 3383 | -0.1% | -396.1 to +388.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 14.97 | 11.78 | -21.3% | -4.176 to -2.194 | GAIN |
| failed requests (%) | 5.187 | 4.256 | -17.9% | -1.591 to -0.2711 | GAIN |
| HPA replicas, mean | 9.506 | 13.97 | +47.0% | +4.174 to +4.755 | power given |
| pods started | 5.902 | 12.56 | +112.8% | +6.132 to +7.185 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.346e-16 to +1.88e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179 | 178.6 | -0.3% | -0.9062 to -0.05092 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179 | 178.6 | -0.3% | -0.9062 to -0.05092 | GAIN |
| CPU used with Omni's own (cores), mean | 1.823 | 1.86 | +2.0% | +0.02543 to +0.04854 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.78 | 56.09 | +2.4% | +0.9615 to +1.647 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1245 | 1217 | -2.2% | -182 to +126.9 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4033 | 4249 | +5.4% | -153.3 to +586.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 20.19 | 15.18 | -24.8% | -6.489 to -3.535 | GAIN |
| failed requests (%) | 8.194 | 6.856 | -16.3% | -2.219 to -0.4588 | GAIN |
| HPA replicas, mean | 9.595 | 14.13 | +47.3% | +4.236 to +4.834 | power given |
| pods started | 5.537 | 12.54 | +126.4% | +6.41 to +7.59 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.057e-16 to +2.024e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.5 | 180 | -0.3% | -1.014 to +0.003688 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.5 | 180 | -0.3% | -1.014 to +0.003688 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.979 | 2.008 | +1.4% | +0.01555 to +0.04098 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.25 | 60.63 | +2.3% | +1.063 to +1.702 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.09024 | +0.0902 | +0.08076 to +0.09973 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Distribution / Specialized

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
