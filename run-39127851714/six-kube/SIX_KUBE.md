# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 100 copies: native | The spine, the muscles every stack runs on, 100 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3380 | 4447 | 4212 | 4067 | 3927 | 3451 | 3166 | 2916 | 3300 | 2874 |
| response time (ms), 99th percentile | 5830 | 6732 | 6856 | 7423 | 6842 | 6248 | 5204 | 4597 | 5583 | 5258 |
| time over the response line (% of samples) | 59.67 | 57.23 | 74.67 | 76.27 | 55.61 | 55.48 | 45.52 | 47.06 | 60.51 | 58.13 |
| failed requests (%) | 48.09 | 47.74 | 59.63 | 62.07 | 40.4 | 40.85 | 34.75 | 38.8 | 49.88 | 50.55 |
| HPA replicas, mean | 9.869 | 13.82 | 9.921 | 12.14 | 9.879 | 13.79 | 9.808 | 11.68 | 9.839 | 11.87 |
| pods started | 2.6 | 6.4 | 1.9 | 4.8 | 2.5 | 7.7 | 3.9 | 6.2 | 3.3 | 5.2 |
| worker nodes in service, mean | 5.99 | 6 | 6 | 6 | 6 | 5.993 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 276.9 | 279.3 | 279.1 | 277.9 | 277.9 | 275.1 | 275.5 | 277 | 277.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.6 | 276.9 | 279.3 | 279.1 | 277.9 | 277.7 | 275.1 | 275.5 | 277 | 277.9 |
| CPU used with Omni's own (cores), mean | 2.45 | 2.487 | 2.633 | 2.657 | 2.512 | 2.549 | 2.346 | 2.403 | 2.487 | 2.519 |
| host CPU busy, the real machine under kind (%) | 73.04 | 77.36 | 80.58 | 87.93 | 76.81 | 81.69 | 71.81 | 78.02 | 75.81 | 82.62 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.43 | 0.53 | 0.99 | 1.29 | 0.69 | 0.46 | 0.7 | 0.43 | 0.56 | 1.03 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3380 | 4447 | +31.6% | +241.2 to +1893 | LOSS |
| response time (ms), 99th percentile | 5830 | 6732 | +15.5% | -162.6 to +1965 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 59.67 | 57.23 | -4.1% | -5.029 to +0.1431 | EVEN, inside the noise (cut) |
| failed requests (%) | 48.09 | 47.74 | -0.7% | -4.415 to +3.709 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.869 | 13.82 | +40.0% | +2.616 to +5.281 | power given |
| pods started | 2.6 | 6.4 | +146.2% | +2.642 to +4.958 | power given |
| worker nodes in service, mean | 5.99 | 6 | +0.2% | -0.01252 to +0.03237 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 276.9 | -0.0% | -0.933 to +0.9308 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.6 | 276.9 | +0.1% | -0.8002 to +1.398 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.45 | 2.487 | +1.5% | +0.001077 to +0.07144 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.04 | 77.36 | +5.9% | +3.515 to +5.132 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.43 | 0.53 | +23.3% | +0.01079 to +0.1892 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4212 | 4067 | -3.4% | -1227 to +938 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6856 | 7423 | +8.3% | -684.9 to +1819 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 74.67 | 76.27 | +2.2% | -2.545 to +5.756 | EVEN, inside the noise (up) |
| failed requests (%) | 59.63 | 62.07 | +4.1% | -2.607 to +7.488 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.921 | 12.14 | +22.4% | +1.033 to +3.405 | power given |
| pods started | 1.9 | 4.8 | +152.6% | +1.267 to +4.533 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.057e-15 to +8.793e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 279.3 | 279.1 | -0.0% | -0.9215 to +0.6835 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 279.3 | 279.1 | -0.0% | -0.9215 to +0.6835 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.633 | 2.657 | +0.9% | +0.01336 to +0.0348 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 80.58 | 87.93 | +9.1% | +6.884 to +7.815 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.99 | 1.29 | +30.3% | +0.1383 to +0.4617 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3927 | 3451 | -12.1% | -2009 to +1058 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6842 | 6248 | -8.7% | -1618 to +429.3 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 55.61 | 55.48 | -0.2% | -2.717 to +2.47 | EVEN, inside the noise (cut) |
| failed requests (%) | 40.4 | 40.85 | +1.1% | -3.033 to +3.938 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.879 | 13.79 | +39.6% | +2.644 to +5.185 | power given |
| pods started | 2.5 | 7.7 | +208.0% | +3.626 to +6.774 | power given |
| worker nodes in service, mean | 6 | 5.993 | -0.1% | -0.02285 to +0.008841 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.9 | 277.9 | +0.0% | -0.9183 to +1.02 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.9 | 277.7 | -0.1% | -1.332 to +1.009 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.512 | 2.549 | +1.5% | +0.01343 to +0.05985 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.81 | 81.69 | +6.4% | +4.444 to +5.315 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.69 | 0.46 | -33.3% | -0.3471 to -0.1129 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 1 (HPA replicas, mean), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3166 | 2916 | -7.9% | -2145 to +1645 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5204 | 4597 | -11.7% | -2450 to +1235 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 45.52 | 47.06 | +3.4% | -1.694 to +4.791 | EVEN, inside the noise (up) |
| failed requests (%) | 34.75 | 38.8 | +11.6% | +0.2977 to +7.798 | LOSS |
| HPA replicas, mean | 9.808 | 11.68 | +19.1% | +0.4317 to +3.313 | power given |
| pods started | 3.9 | 6.2 | +59.0% | -0.2912 to +4.891 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.494e-16 to +6.718e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.1 | 275.5 | +0.1% | -1.213 to +1.972 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.1 | 275.5 | +0.1% | -1.213 to +1.972 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.346 | 2.403 | +2.4% | +0.001229 to +0.1126 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.81 | 78.02 | +8.6% | +4.841 to +7.569 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.7 | 0.43 | -38.6% | -0.421 to -0.119 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 5 (HPA replicas, mean; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3300 | 2874 | -12.9% | -2176 to +1323 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5583 | 5258 | -5.8% | -1845 to +1196 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 60.51 | 58.13 | -3.9% | -4.4 to -0.3572 | GAIN |
| failed requests (%) | 49.88 | 50.55 | +1.3% | -2.939 to +4.279 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.839 | 11.87 | +20.7% | +0.4768 to +3.589 | power given |
| pods started | 3.3 | 5.2 | +57.6% | -0.3733 to +4.173 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.236e-15 to +9.925e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277 | 277.9 | +0.3% | +0.08168 to +1.742 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277 | 277.9 | +0.3% | +0.08168 to +1.742 | power given |
| CPU used with Omni's own (cores), mean | 2.487 | 2.519 | +1.3% | +0.003574 to +0.06173 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.81 | 82.62 | +9.0% | +5.991 to +7.64 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.56 | 1.03 | +83.9% | +0.3392 to +0.6008 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
