# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 100 copies: native | The spine, the muscles every stack runs on, 100 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 4247 | 3797 | 4199 | 3922 | 3250 | 3057 | 4118 | 3420 | 3245 | 3095 |
| response time (ms), 99th percentile | 6306 | 6124 | 6254 | 5822 | 5068 | 4910 | 6291 | 5639 | 5452 | 5364 |
| time over the response line (% of samples) | 50.38 | 50.72 | 54.69 | 56.21 | 42.1 | 41.51 | 49.43 | 50.32 | 49.97 | 52.73 |
| failed requests (%) | 30.79 | 33.33 | 38.56 | 42.2 | 28.56 | 30.25 | 32.92 | 35.26 | 35.08 | 39.56 |
| HPA replicas, mean | 9.77 | 12.63 | 9.816 | 11.31 | 9.772 | 12.35 | 9.777 | 11.72 | 9.767 | 11.68 |
| pods started | 4.775 | 10.38 | 4.125 | 7.35 | 4.65 | 10.62 | 4.8 | 8.55 | 4.95 | 9.1 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 5.999 | 6 | 6 | 6 | 5.998 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.2 | 276.2 | 277.3 | 276.9 | 274.4 | 274 | 276.8 | 276.4 | 277.2 | 276.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.2 | 276.2 | 277.3 | 276.9 | 274.4 | 274 | 276.8 | 276.4 | 277.2 | 276.6 |
| CPU used with Omni's own (cores), mean | 2.433 | 2.475 | 2.459 | 2.512 | 2.286 | 2.335 | 2.428 | 2.476 | 2.475 | 2.522 |
| host CPU busy, the real machine under kind (%) | 71.71 | 76.33 | 74.86 | 83.22 | 69.78 | 75.53 | 74.16 | 80.54 | 74.47 | 82.18 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.445 | 0.5075 | 0.795 | 1.188 | 0.6175 | 0.3775 | 0.7225 | 0.4 | 0.5025 | 1.045 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4247 | 3797 | -10.6% | -1039 to +139.6 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6306 | 6124 | -2.9% | -618 to +254.5 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 50.38 | 50.72 | +0.7% | -1.133 to +1.818 | STEADY, inside the noise (up) |
| failed requests (%) | 30.79 | 33.33 | +8.3% | +0.7612 to +4.325 | LOSS |
| HPA replicas, mean | 9.77 | 12.63 | +29.3% | +2.247 to +3.474 | power given |
| pods started | 4.775 | 10.38 | +117.3% | +4.662 to +6.538 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.05e-16 to +3.498e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.2 | 276.2 | +0.0% | -0.5281 to +0.6296 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.2 | 276.2 | +0.0% | -0.5281 to +0.6296 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.433 | 2.475 | +1.7% | +0.03049 to +0.05317 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.71 | 76.33 | +6.4% | +4.346 to +4.894 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.445 | 0.5075 | +14.0% | +0.01042 to +0.1146 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4199 | 3922 | -6.6% | -1071 to +515.9 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6254 | 5822 | -6.9% | -1108 to +242.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 54.69 | 56.21 | +2.8% | -0.4719 to +3.499 | STEADY, inside the noise (up) |
| failed requests (%) | 38.56 | 42.2 | +9.4% | +0.5061 to +6.771 | LOSS |
| HPA replicas, mean | 9.816 | 11.31 | +15.3% | +0.7677 to +2.23 | power given |
| pods started | 4.125 | 7.35 | +78.2% | +2.274 to +4.176 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.103e-16 to +1.133e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.3 | 276.9 | -0.1% | -0.9024 to +0.2091 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.3 | 276.9 | -0.1% | -0.9024 to +0.2091 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.459 | 2.512 | +2.1% | +0.02415 to +0.08063 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.86 | 83.22 | +11.2% | +7.683 to +9.025 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.795 | 1.188 | +49.4% | +0.3117 to +0.4733 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3250 | 3057 | -5.9% | -686.5 to +300.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5068 | 4910 | -3.1% | -710.9 to +396.3 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 42.1 | 41.51 | -1.4% | -1.707 to +0.5243 | STEADY, inside the noise (cut) |
| failed requests (%) | 28.56 | 30.25 | +5.9% | -0.6475 to +4.024 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.772 | 12.35 | +26.4% | +1.878 to +3.277 | power given |
| pods started | 4.65 | 10.62 | +128.5% | +4.819 to +7.131 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003556 to +0.001204 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 274.4 | 274 | -0.2% | -1.018 to +0.1668 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.4 | 274 | -0.2% | -1.099 to +0.1773 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.286 | 2.335 | +2.2% | +0.03136 to +0.06717 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.78 | 75.53 | +8.2% | +5.318 to +6.178 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.6175 | 0.3775 | -38.9% | -0.2827 to -0.1973 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4118 | 3420 | -17.0% | -1652 to +256.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6291 | 5639 | -10.4% | -1444 to +140.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 49.43 | 50.32 | +1.8% | -0.7774 to +2.567 | STEADY, inside the noise (up) |
| failed requests (%) | 32.92 | 35.26 | +7.1% | -0.6732 to +5.337 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.777 | 11.72 | +19.9% | +1.217 to +2.665 | power given |
| pods started | 4.8 | 8.55 | +78.1% | +2.765 to +4.735 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.428e-16 to +1.367e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.8 | 276.4 | -0.1% | -0.9941 to +0.1699 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.8 | 276.4 | -0.1% | -0.9941 to +0.1699 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.428 | 2.476 | +2.0% | +0.02538 to +0.06932 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.16 | 80.54 | +8.6% | +5.815 to +6.959 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.7225 | 0.4 | -44.6% | -0.3788 to -0.2662 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3245 | 3095 | -4.6% | -973 to +673.6 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5452 | 5364 | -1.6% | -981.7 to +805 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 49.97 | 52.73 | +5.5% | +0.3059 to +5.203 | LOSS |
| failed requests (%) | 35.08 | 39.56 | +12.8% | +0.7444 to +8.216 | LOSS |
| HPA replicas, mean | 9.767 | 11.68 | +19.6% | +1.183 to +2.647 | power given |
| pods started | 4.95 | 9.1 | +83.8% | +3.409 to +4.891 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.004723 to +0.001598 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.2 | 276.7 | -0.2% | -1.212 to +0.2527 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.2 | 276.6 | -0.2% | -1.339 to +0.2849 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.475 | 2.522 | +1.9% | +0.02534 to +0.06825 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.47 | 82.18 | +10.3% | +7.319 to +8.095 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.5025 | 1.045 | +108.0% | +0.4807 to +0.6043 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
