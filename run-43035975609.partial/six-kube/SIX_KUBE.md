# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 100 copies: native | The spine, the muscles every stack runs on, 100 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3894 | 3085 | 4603 | 3988 | 4221 | 3361 |
| response time (ms), 99th percentile | 5816 | 5387 | 6928 | 6176 | 6482 | 5892 |
| time over the response line (% of samples) | 47.95 | 49.18 | 61.21 | 60.75 | 53.13 | 53.46 |
| failed requests (%) | 31.36 | 36.1 | 44.12 | 46.58 | 35.25 | 38.4 |
| HPA replicas, mean | 9.792 | 12.83 | 9.815 | 10.99 | 9.794 | 11.97 |
| pods started | 4.241 | 9.614 | 4.145 | 6.817 | 4.434 | 9.012 |
| worker nodes in service, mean | 6 | 5.999 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.7 | 276.1 | 278.1 | 277.6 | 277.2 | 277 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.7 | 276.1 | 278.1 | 277.6 | 277.2 | 277 |
| CPU used with Omni's own (cores), mean | 2.388 | 2.439 | 2.528 | 2.562 | 2.462 | 2.504 |
| host CPU busy, the real machine under kind (%) | 71.1 | 75.9 | 76.82 | 84.85 | 75.16 | 80.68 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 |
| organism behind its window (s) | 0.5036 | 5.722 | 0.9301 | 1.191 | 0.6145 | 0.4386 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 2 (time over the response line (% of samples); failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1; OFF THE CLOCK in 1 of 83 repetitions (the organism ended up to 431 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

83 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3894 | 3085 | -20.8% | -1226 to -390.8 | GAIN |
| response time (ms), 99th percentile | 5816 | 5387 | -7.4% | -782.4 to -74.69 | GAIN |
| time over the response line (% of samples) | 47.95 | 49.18 | +2.6% | +0.1527 to +2.3 | LOSS |
| failed requests (%) | 31.36 | 36.1 | +15.1% | +3.193 to +6.296 | LOSS |
| HPA replicas, mean | 9.792 | 12.83 | +31.0% | +2.586 to +3.493 | power given |
| pods started | 4.241 | 9.614 | +126.7% | +4.821 to +5.926 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003933 to +0.001301 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.7 | 276.1 | +0.1% | +0.0689 to +0.7558 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.7 | 276.1 | +0.1% | +0.01775 to +0.7266 | power given |
| CPU used with Omni's own (cores), mean | 2.388 | 2.439 | +2.1% | +0.04103 to +0.06014 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.1 | 75.9 | +6.7% | +4.552 to +5.044 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.5036 | 5.722 | +1036.1% | -4.989 to +15.42 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 5 (response time (ms), 95th percentile; response time (ms), 99th percentile; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 1

82 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4603 | 3988 | -13.4% | -1089 to -141.4 | GAIN |
| response time (ms), 99th percentile | 6927 | 6176 | -10.8% | -1218 to -284.5 | GAIN |
| time over the response line (% of samples) | 61.03 | 60.75 | -0.5% | -1.224 to +0.6644 | STEADY, inside the noise (cut) |
| failed requests (%) | 43.92 | 46.58 | +6.1% | +0.8338 to +4.484 | LOSS |
| HPA replicas, mean | 9.814 | 10.99 | +12.0% | +0.7452 to +1.615 | power given |
| pods started | 4.183 | 6.817 | +63.0% | +1.945 to +3.323 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.946e-16 to +9.969e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 278.1 | 277.6 | -0.2% | -0.8232 to -0.1601 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.1 | 277.6 | -0.2% | -0.8232 to -0.1601 | GAIN |
| CPU used with Omni's own (cores), mean | 2.527 | 2.562 | +1.4% | +0.02183 to +0.04779 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.77 | 84.85 | +10.5% | +7.766 to +8.406 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.9244 | 1.191 | +28.9% | +0.2242 to +0.3099 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

83 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4221 | 3361 | -20.4% | -1350 to -369.9 | GAIN |
| response time (ms), 99th percentile | 6482 | 5892 | -9.1% | -1057 to -124.3 | GAIN |
| time over the response line (% of samples) | 53.13 | 53.46 | +0.6% | -0.4945 to +1.159 | STEADY, inside the noise (up) |
| failed requests (%) | 35.25 | 38.4 | +9.0% | +1.468 to +4.842 | LOSS |
| HPA replicas, mean | 9.794 | 11.97 | +22.3% | +1.733 to +2.628 | power given |
| pods started | 4.434 | 9.012 | +103.3% | +3.914 to +5.243 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +7.604e-17 to +8.87e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.2 | 277 | -0.1% | -0.5718 to +0.08394 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.2 | 277 | -0.1% | -0.5718 to +0.08394 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.462 | 2.504 | +1.7% | +0.0332 to +0.0519 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.16 | 80.68 | +7.3% | +5.308 to +5.732 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.6145 | 0.4386 | -28.6% | -0.2204 to -0.1314 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Energy / Facility / Industrial
- Distribution / Specialized
- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
