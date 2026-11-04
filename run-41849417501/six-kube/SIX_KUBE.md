# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 100 copies: native | The spine, the muscles every stack runs on, 100 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2992 | 2871 | 4635 | 5110 | 3429 | 2189 | 4219 | 2225 | 3083 | 2670 |
| response time (ms), 99th percentile | 5551 | 5667 | 7265 | 7475 | 5972 | 5152 | 5742 | 4446 | 6128 | 5255 |
| time over the response line (% of samples) | 52.94 | 54.34 | 64.24 | 64.48 | 45.88 | 44.92 | 51.78 | 50.08 | 63.24 | 62.91 |
| failed requests (%) | 37.76 | 40.18 | 46.98 | 45.85 | 29.95 | 34.26 | 36.91 | 42.31 | 50.58 | 50.18 |
| HPA replicas, mean | 9.84 | 12.14 | 9.814 | 10.93 | 9.77 | 12.36 | 9.804 | 11.87 | 9.828 | 11.5 |
| pods started | 3.2 | 9.2 | 4.4 | 8.4 | 4.8 | 9.5 | 4 | 9.7 | 4.1 | 7.9 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.996 | 6 | 5.984 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.7 | 276.9 | 279.2 | 278.6 | 275.2 | 276.2 | 276.5 | 275.8 | 278 | 277.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.7 | 276.9 | 279.2 | 278.6 | 275.2 | 276.2 | 276.5 | 275.7 | 278 | 276.8 |
| CPU used with Omni's own (cores), mean | 2.458 | 2.514 | 2.584 | 2.602 | 2.344 | 2.397 | 2.414 | 2.465 | 2.57 | 2.603 |
| host CPU busy, the real machine under kind (%) | 72.83 | 77.79 | 77.66 | 85.33 | 71.69 | 77.2 | 74.02 | 80.27 | 77.14 | 84.6 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.42 | 0.49 | 0.87 | 1.17 | 0.55 | 0.39 | 0.85 | 0.38 | 0.48 | 1.1 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2992 | 2871 | -4.0% | -1203 to +960.9 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5551 | 5667 | +2.1% | -1714 to +1945 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 52.94 | 54.34 | +2.6% | -1.435 to +4.24 | STEADY, inside the noise (up) |
| failed requests (%) | 37.76 | 40.18 | +6.4% | -1.64 to +6.481 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.84 | 12.14 | +23.4% | +0.7057 to +3.896 | power given |
| pods started | 3.2 | 9.2 | +187.5% | +4.455 to +7.545 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.694e-16 to +1.535e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.7 | 276.9 | +0.1% | -1.006 to +1.411 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.7 | 276.9 | +0.1% | -1.006 to +1.411 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.458 | 2.514 | +2.3% | +0.02108 to +0.08991 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.83 | 77.79 | +6.8% | +4.13 to +5.796 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.42 | 0.49 | +16.7% | +0.01111 to +0.1289 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 3 (pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4635 | 5110 | +10.3% | -1156 to +2106 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 7265 | 7475 | +2.9% | -830.1 to +1250 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 64.24 | 64.48 | +0.4% | -3.246 to +3.73 | STEADY, inside the noise (up) |
| failed requests (%) | 46.98 | 45.85 | -2.4% | -7.995 to +5.729 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.814 | 10.93 | +11.3% | -0.2572 to +2.483 | STEADY, inside the noise (up) |
| pods started | 4.4 | 8.4 | +90.9% | +1.664 to +6.336 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.42e-16 to +2.396e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 279.2 | 278.6 | -0.2% | -1.201 to +0.05123 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 279.2 | 278.6 | -0.2% | -1.201 to +0.05123 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.584 | 2.602 | +0.7% | -0.01133 to +0.04753 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.66 | 85.33 | +9.9% | +7.101 to +8.239 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.87 | 1.17 | +34.5% | +0.1882 to +0.4118 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3429 | 2189 | -36.2% | -3074 to +594.9 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5972 | 5152 | -13.7% | -1827 to +185 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 45.88 | 44.92 | -2.1% | -4.309 to +2.38 | STEADY, inside the noise (cut) |
| failed requests (%) | 29.95 | 34.26 | +14.4% | +0.5818 to +8.043 | LOSS |
| HPA replicas, mean | 9.77 | 12.36 | +26.5% | +0.8692 to +4.302 | power given |
| pods started | 4.8 | 9.5 | +97.9% | +2.462 to +6.938 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.012e-16 to +1.312e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.2 | 276.2 | +0.4% | -0.2405 to +2.306 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.2 | 276.2 | +0.4% | -0.2405 to +2.306 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.344 | 2.397 | +2.2% | +0.02356 to +0.08177 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.69 | 77.2 | +7.7% | +4.82 to +6.199 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.55 | 0.39 | -29.1% | -0.2203 to -0.09968 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4219 | 2225 | -47.3% | -3705 to -283.8 | GAIN |
| response time (ms), 99th percentile | 5742 | 4446 | -22.6% | -3397 to +804.5 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 51.78 | 50.08 | -3.3% | -4.115 to +0.7075 | STEADY, inside the noise (cut) |
| failed requests (%) | 36.91 | 42.31 | +14.6% | +0.01265 to +10.79 | LOSS |
| HPA replicas, mean | 9.804 | 11.87 | +21.1% | +0.4397 to +3.699 | power given |
| pods started | 4 | 9.7 | +142.5% | +2.96 to +8.44 | power given |
| worker nodes in service, mean | 6 | 5.996 | -0.1% | -0.01153 to +0.00446 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.5 | 275.8 | -0.2% | -2.311 to +0.9759 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.5 | 275.7 | -0.3% | -2.518 to +0.9702 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.414 | 2.465 | +2.1% | +0.01559 to +0.08635 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.02 | 80.27 | +8.4% | +5.547 to +6.958 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.85 | 0.38 | -55.3% | -0.6639 to -0.2761 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3083 | 2670 | -13.4% | -2862 to +2036 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6128 | 5255 | -14.2% | -2851 to +1106 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 63.24 | 62.91 | -0.5% | -2.285 to +1.613 | STEADY, inside the noise (cut) |
| failed requests (%) | 50.58 | 50.18 | -0.8% | -7.942 to +7.152 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.828 | 11.5 | +17.0% | +0.2068 to +3.141 | power given |
| pods started | 4.1 | 7.9 | +92.7% | +1.929 to +5.671 | power given |
| worker nodes in service, mean | 6 | 5.984 | -0.3% | -0.05105 to +0.01975 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 278 | 277.3 | -0.3% | -4.524 to +3.113 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278 | 276.8 | -0.4% | -6.047 to +3.685 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.57 | 2.603 | +1.3% | -0.01271 to +0.07904 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.14 | 84.6 | +9.7% | +6.226 to +8.689 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.48 | 1.1 | +129.2% | +0.5321 to +0.7079 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
