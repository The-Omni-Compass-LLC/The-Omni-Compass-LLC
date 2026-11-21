# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3559 | 2760 | 3841 | 3034 | 4477 | 3603 | 2661 | 1806 |
| response time (ms), 99th percentile | 5870 | 5452 | 6198 | 5929 | 7308 | 6407 | 4647 | 4185 |
| time over the response line (% of samples) | 58.89 | 57.38 | 54.04 | 53.98 | 62.17 | 61.9 | 43.95 | 43.81 |
| failed requests (%) | 45.1 | 48.25 | 39.69 | 44.85 | 45.33 | 51.46 | 33.26 | 36.15 |
| HPA replicas, mean | 9.829 | 12.18 | 9.84 | 12.67 | 9.859 | 11.77 | 9.774 | 12.66 |
| pods started | 3.679 | 5.786 | 3.25 | 6.964 | 3.107 | 5.071 | 4.607 | 7.964 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.999 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 276.7 | 276.6 | 277.4 | 278.5 | 278.8 | 275.3 | 276.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 276.7 | 276.6 | 277.3 | 278.5 | 278.8 | 275.3 | 276.2 |
| CPU used with Omni's own (cores), mean | 2.478 | 2.507 | 2.447 | 2.481 | 2.562 | 2.592 | 2.384 | 2.426 |
| host CPU busy, the real machine under kind (%) | 75.12 | 82.4 | 74.8 | 79.9 | 78.57 | 83.98 | 71.53 | 78.53 |
| organism work | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.7714 | 1.164 | 0.6 | 0.475 | 0.7643 | 0.4464 | 0.4679 | 1.046 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (failed requests (%); organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

28 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3559 | 2760 | -22.5% | -1697 to +99.1 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5870 | 5452 | -7.1% | -1036 to +201.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 58.89 | 57.38 | -2.6% | -2.765 to -0.2571 | GAIN |
| failed requests (%) | 45.1 | 48.25 | +7.0% | +1.228 to +5.066 | LOSS |
| HPA replicas, mean | 9.829 | 12.18 | +23.9% | +1.664 to +3.03 | power given |
| pods started | 3.679 | 5.786 | +57.3% | +1.299 to +2.916 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.727e-15 to +1.387e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 276.7 | -0.1% | -1.257 to +0.8285 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 276.7 | -0.1% | -1.257 to +0.8285 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.478 | 2.507 | +1.1% | +0.01412 to +0.04274 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.12 | 82.4 | +9.7% | +6.964 to +7.597 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | LOSS |
| organism behind its window (s) | 0.7714 | 1.164 | +50.9% | +0.2658 to +0.5199 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (failed requests (%); organism work per energy), power given on 5 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J)), EVEN (inside the noise) on 4

28 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3841 | 3034 | -21.0% | -1705 to +90.18 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6198 | 5929 | -4.3% | -957.1 to +419.9 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 54.04 | 53.98 | -0.1% | -1.231 to +1.111 | EVEN, inside the noise (cut) |
| failed requests (%) | 39.69 | 44.85 | +13.0% | +2.654 to +7.683 | LOSS |
| HPA replicas, mean | 9.84 | 12.67 | +28.7% | +2.117 to +3.54 | power given |
| pods started | 3.25 | 6.964 | +114.3% | +2.634 to +4.795 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003959 to +0.001284 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.6 | 277.4 | +0.3% | +0.1197 to +1.447 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.6 | 277.3 | +0.3% | +0.05555 to +1.431 | power given |
| CPU used with Omni's own (cores), mean | 2.447 | 2.481 | +1.4% | +0.01742 to +0.05104 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.8 | 79.9 | +6.8% | +4.661 to +5.544 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | LOSS |
| organism behind its window (s) | 0.6 | 0.475 | -20.8% | -0.2054 to -0.04459 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

28 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4477 | 3603 | -19.5% | -2116 to +368 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 7308 | 6407 | -12.3% | -1893 to +91.78 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 62.17 | 61.9 | -0.4% | -2.093 to +1.561 | EVEN, inside the noise (cut) |
| failed requests (%) | 45.33 | 51.46 | +13.5% | +3.806 to +8.443 | LOSS |
| HPA replicas, mean | 9.859 | 11.77 | +19.3% | +1.185 to +2.63 | power given |
| pods started | 3.107 | 5.071 | +63.2% | +0.8623 to +3.066 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.199e-15 to +1.208e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 278.5 | 278.8 | +0.1% | -0.3428 to +0.9082 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.5 | 278.8 | +0.1% | -0.3428 to +0.9082 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.562 | 2.592 | +1.2% | +0.01773 to +0.04244 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.57 | 83.98 | +6.9% | +5.096 to +5.725 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.7643 | 0.4464 | -41.6% | -0.4034 to -0.2323 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 5 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J)), EVEN (inside the noise) on 3

28 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2661 | 1806 | -32.1% | -1578 to -131.8 | GAIN |
| response time (ms), 99th percentile | 4647 | 4185 | -9.9% | -1027 to +103.9 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 43.95 | 43.81 | -0.3% | -2.79 to +2.504 | EVEN, inside the noise (cut) |
| failed requests (%) | 33.26 | 36.15 | +8.7% | -0.4301 to +6.199 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.774 | 12.66 | +29.6% | +2.09 to +3.688 | power given |
| pods started | 4.607 | 7.964 | +72.9% | +2.308 to +4.406 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.053e-15 to -2.158e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.3 | 276.2 | +0.3% | +0.2321 to +1.431 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.3 | 276.2 | +0.3% | +0.2321 to +1.431 | power given |
| CPU used with Omni's own (cores), mean | 2.384 | 2.426 | +1.7% | +0.02449 to +0.05839 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.53 | 78.53 | +9.8% | +6.582 to +7.409 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | LOSS |
| organism behind its window (s) | 0.4679 | 1.046 | +123.7% | +0.4977 to +0.6594 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
