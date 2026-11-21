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
| response time (ms), 95th percentile | 3430 | 2628 | 3964 | 2843 | 2923 | 2247 | 3701 | 2378 |
| response time (ms), 99th percentile | 5634 | 5203 | 6170 | 5422 | 5114 | 4850 | 5799 | 4967 |
| time over the response line (% of samples) | 56.78 | 56.32 | 56.85 | 55.78 | 51.13 | 50.19 | 56.57 | 55.8 |
| failed requests (%) | 44.42 | 48.18 | 42.16 | 47.68 | 39.74 | 43.81 | 46.11 | 49.4 |
| HPA replicas, mean | 9.86 | 12.21 | 9.848 | 12.62 | 9.837 | 12.53 | 9.838 | 12.83 |
| pods started | 2.952 | 5.806 | 3.339 | 6.323 | 3.306 | 6.71 | 3.29 | 6.5 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.998 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.8 | 277.2 | 277 | 277.4 | 275.8 | 276.2 | 276.7 | 277.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.8 | 277.2 | 277 | 277.4 | 275.8 | 276.2 | 276.7 | 277.4 |
| CPU used with Omni's own (cores), mean | 2.462 | 2.507 | 2.478 | 2.509 | 2.387 | 2.424 | 2.46 | 2.501 |
| host CPU busy, the real machine under kind (%) | 74.94 | 82.7 | 75.79 | 80.61 | 73.6 | 79.27 | 74.62 | 81.77 |
| organism work | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.8081 | 1.218 | 0.6774 | 0.4274 | 0.6742 | 0.4758 | 0.5177 | 1.123 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 100 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 2 (failed requests (%); organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 5

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3430 | 2628 | -23.4% | -1258 to -345.6 | GAIN |
| response time (ms), 99th percentile | 5634 | 5203 | -7.7% | -950.7 to +88.29 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 56.78 | 56.32 | -0.8% | -1.497 to +0.5757 | EVEN, inside the noise (cut) |
| failed requests (%) | 44.42 | 48.18 | +8.5% | +2.617 to +4.902 | LOSS |
| HPA replicas, mean | 9.86 | 12.21 | +23.8% | +1.94 to +2.754 | power given |
| pods started | 2.952 | 5.806 | +96.7% | +2.232 to +3.478 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.001181 to +0.0003831 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.8 | 277.2 | +0.1% | -0.1679 to +0.9946 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.8 | 277.2 | +0.1% | -0.1785 to +0.9809 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.462 | 2.507 | +1.9% | +0.03259 to +0.05875 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.94 | 82.7 | +10.4% | +7.373 to +8.151 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | LOSS |
| organism behind its window (s) | 0.8081 | 1.218 | +50.7% | +0.3218 to +0.4975 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (failed requests (%); organism work per energy), power given on 5 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J)), EVEN (inside the noise) on 1

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3964 | 2843 | -28.3% | -1752 to -488.5 | GAIN |
| response time (ms), 99th percentile | 6170 | 5422 | -12.1% | -1376 to -119.8 | GAIN |
| time over the response line (% of samples) | 56.85 | 55.78 | -1.9% | -2.049 to -0.09347 | GAIN |
| failed requests (%) | 42.16 | 47.68 | +13.1% | +3.752 to +7.295 | LOSS |
| HPA replicas, mean | 9.848 | 12.62 | +28.1% | +2.285 to +3.259 | power given |
| pods started | 3.339 | 6.323 | +89.4% | +2.294 to +3.674 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.004912 to +0.001593 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 277 | 277.4 | +0.2% | +0.1199 to +0.7913 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277 | 277.4 | +0.1% | +0.06195 to +0.7484 | power given |
| CPU used with Omni's own (cores), mean | 2.478 | 2.509 | +1.3% | +0.02319 to +0.03971 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.79 | 80.61 | +6.4% | +4.585 to +5.052 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | LOSS |
| organism behind its window (s) | 0.6774 | 0.4274 | -36.9% | -0.3179 to -0.1821 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2923 | 2247 | -23.1% | -1202 to -151.5 | GAIN |
| response time (ms), 99th percentile | 5114 | 4850 | -5.2% | -843.8 to +317.1 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 51.13 | 50.19 | -1.8% | -1.94 to +0.06178 | EVEN, inside the noise (cut) |
| failed requests (%) | 39.74 | 43.81 | +10.2% | +2.881 to +5.263 | LOSS |
| HPA replicas, mean | 9.837 | 12.53 | +27.3% | +2.265 to +3.116 | power given |
| pods started | 3.306 | 6.71 | +102.9% | +2.673 to +4.133 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.975e-16 to +2.683e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.8 | 276.2 | +0.2% | +0.1164 to +0.798 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.8 | 276.2 | +0.2% | +0.1164 to +0.798 | power given |
| CPU used with Omni's own (cores), mean | 2.387 | 2.424 | +1.6% | +0.0269 to +0.04712 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.6 | 79.27 | +7.7% | +5.369 to +5.955 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.6742 | 0.4758 | -29.4% | -0.2584 to -0.1383 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 2 (failed requests (%); organism work per energy), power given on 5 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J)), EVEN (inside the noise) on 1

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3701 | 2378 | -35.7% | -1848 to -796.1 | GAIN |
| response time (ms), 99th percentile | 5799 | 4967 | -14.4% | -1345 to -319.7 | GAIN |
| time over the response line (% of samples) | 56.57 | 55.8 | -1.4% | -1.598 to +0.0673 | EVEN, inside the noise (cut) |
| failed requests (%) | 46.11 | 49.4 | +7.1% | +2.27 to +4.297 | LOSS |
| HPA replicas, mean | 9.838 | 12.83 | +30.4% | +2.544 to +3.443 | power given |
| pods started | 3.29 | 6.5 | +97.5% | +2.536 to +3.883 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.217e-16 to +3.925e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.7 | 277.4 | +0.3% | +0.3535 to +1.088 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.7 | 277.4 | +0.3% | +0.3535 to +1.088 | power given |
| CPU used with Omni's own (cores), mean | 2.46 | 2.501 | +1.7% | +0.02866 to +0.05462 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.62 | 81.77 | +9.6% | +6.837 to +7.468 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | LOSS |
| organism behind its window (s) | 0.5177 | 1.123 | +116.8% | +0.5396 to +0.6701 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
