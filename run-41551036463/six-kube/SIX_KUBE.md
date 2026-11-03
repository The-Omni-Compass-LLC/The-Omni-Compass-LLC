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
| response time (ms), 95th percentile | 3823 | 2580 | 4223 | 4465 | 2239 | 2118 | 3257 | 2779 | 4130 | 4033 |
| response time (ms), 99th percentile | 5748 | 5511 | 6745 | 6981 | 4551 | 4173 | 4918 | 4470 | 6574 | 6024 |
| time over the response line (% of samples) | 58.29 | 56.75 | 63.64 | 64.83 | 39.66 | 39.59 | 37.06 | 37.71 | 52.39 | 55.82 |
| failed requests (%) | 42.22 | 48.93 | 44.9 | 49.76 | 28.05 | 29.62 | 24.36 | 25.48 | 36.95 | 38.53 |
| HPA replicas, mean | 9.826 | 12.47 | 9.856 | 10.62 | 9.739 | 12.08 | 9.732 | 12.54 | 9.831 | 11.83 |
| pods started | 3.6 | 8.3 | 3.3 | 6 | 5.2 | 11.2 | 5.3 | 11.5 | 3.6 | 7.6 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.995 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 277.5 | 277.3 | 278 | 277.9 | 273.4 | 274.2 | 273.5 | 274.1 | 277.6 | 277.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.5 | 277.3 | 278 | 277.7 | 273.4 | 274.2 | 273.5 | 274.1 | 277.6 | 277.4 |
| CPU used with Omni's own (cores), mean | 2.471 | 2.512 | 2.539 | 2.572 | 2.252 | 2.31 | 2.241 | 2.3 | 2.472 | 2.525 |
| host CPU busy, the real machine under kind (%) | 73.11 | 77.52 | 76.96 | 84.8 | 68.77 | 74.47 | 68.48 | 74.6 | 74.56 | 82.24 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.51 | 0.59 | 0.91 | 1.17 | 0.53 | 0.38 | 0.63 | 0.41 | 0.5 | 1.01 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3823 | 2580 | -32.5% | -2874 to +387.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5748 | 5511 | -4.1% | -2262 to +1788 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 58.29 | 56.75 | -2.7% | -5.094 to +1.999 | STEADY, inside the noise (cut) |
| failed requests (%) | 42.22 | 48.93 | +15.9% | +0.697 to +12.72 | LOSS |
| HPA replicas, mean | 9.826 | 12.47 | +26.9% | +1.36 to +3.932 | power given |
| pods started | 3.6 | 8.3 | +130.6% | +3.308 to +6.092 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.623e-15 to +3.141e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.5 | 277.3 | -0.1% | -1.008 to +0.65 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.5 | 277.3 | -0.1% | -1.008 to +0.65 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.471 | 2.512 | +1.6% | +0.02834 to +0.05308 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.11 | 77.52 | +6.0% | +4.208 to +4.607 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.51 | 0.59 | +15.7% | -0.2212 to +0.3812 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 3 (pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 8

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4223 | 4465 | +5.7% | -1574 to +2058 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6745 | 6981 | +3.5% | -1568 to +2040 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 63.64 | 64.83 | +1.9% | -3.836 to +6.214 | STEADY, inside the noise (up) |
| failed requests (%) | 44.9 | 49.76 | +10.8% | -2.583 to +12.31 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.856 | 10.62 | +7.7% | -0.4169 to +1.944 | STEADY, inside the noise (up) |
| pods started | 3.3 | 6 | +81.8% | +0.5134 to +4.887 | power given |
| worker nodes in service, mean | 6 | 5.995 | -0.1% | -0.01536 to +0.005943 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 278 | 277.9 | -0.0% | -1.461 to +1.307 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278 | 277.7 | -0.1% | -1.733 to +1.295 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.539 | 2.572 | +1.3% | +0.001627 to +0.06387 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.96 | 84.8 | +10.2% | +7.229 to +8.453 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.91 | 1.17 | +28.6% | +0.06866 to +0.4513 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2239 | 2118 | -5.4% | -1201 to +959 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4551 | 4173 | -8.3% | -1222 to +465.9 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 39.66 | 39.59 | -0.2% | -3.54 to +3.405 | STEADY, inside the noise (cut) |
| failed requests (%) | 28.05 | 29.62 | +5.6% | -3.287 to +6.441 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.739 | 12.08 | +24.0% | +0.8431 to +3.84 | power given |
| pods started | 5.2 | 11.2 | +115.4% | +3.159 to +8.841 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.104e-16 to +7.88e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 274.2 | +0.3% | +0.143 to +1.566 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 274.2 | +0.3% | +0.143 to +1.566 | power given |
| CPU used with Omni's own (cores), mean | 2.252 | 2.31 | +2.6% | +0.01744 to +0.09834 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.77 | 74.47 | +8.3% | +4.814 to +6.597 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.53 | 0.38 | -28.3% | -0.2526 to -0.04744 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3257 | 2779 | -14.7% | -1568 to +611.9 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4918 | 4470 | -9.1% | -1659 to +764.1 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 37.06 | 37.71 | +1.8% | -3.404 to +4.71 | STEADY, inside the noise (up) |
| failed requests (%) | 24.36 | 25.48 | +4.6% | -2.615 to +4.856 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.732 | 12.54 | +28.9% | +1.656 to +3.965 | power given |
| pods started | 5.3 | 11.5 | +117.0% | +3.04 to +9.36 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.215e-16 to +2.12e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 274.1 | +0.2% | -0.7731 to +1.83 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 274.1 | +0.2% | -0.7731 to +1.83 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.241 | 2.3 | +2.6% | +0.02791 to +0.08929 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.48 | 74.6 | +8.9% | +5.36 to +6.885 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.63 | 0.41 | -34.9% | -0.3142 to -0.1258 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4130 | 4033 | -2.3% | -1744 to +1551 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6574 | 6024 | -8.4% | -1820 to +720.1 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 52.39 | 55.82 | +6.6% | -2.684 to +9.553 | STEADY, inside the noise (up) |
| failed requests (%) | 36.95 | 38.53 | +4.3% | -5.817 to +8.976 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.831 | 11.83 | +20.3% | +0.3773 to +3.617 | power given |
| pods started | 3.6 | 7.6 | +111.1% | +1.841 to +6.159 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.108e-15 to +1.641e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.6 | 277.4 | -0.1% | -0.9721 to +0.6563 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.6 | 277.4 | -0.1% | -0.9721 to +0.6563 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.472 | 2.525 | +2.2% | +0.006001 to +0.1003 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.56 | 82.24 | +10.3% | +6.865 to +8.492 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.5 | 1.01 | +102.0% | +0.412 to +0.608 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
