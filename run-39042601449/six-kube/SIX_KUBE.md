# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1555 | 1420 | 1814 | 1791 | 1776 | 1869 | 1597 | 1408 |
| response time (ms), 99th percentile | 5235 | 5131 | 5368 | 5532 | 5599 | 5407 | 4357 | 4526 |
| time over the response line (% of samples) | 24.28 | 16.13 | 19.38 | 14.51 | 19.89 | 14.33 | 23.05 | 16.75 |
| failed requests (%) | 9.999 | 7.979 | 6.466 | 5.948 | 6.685 | 5.761 | 7.045 | 6.621 |
| HPA replicas, mean | 9.649 | 12.88 | 9.625 | 13.45 | 9.621 | 13.47 | 9.578 | 13.41 |
| pods started | 5.323 | 10.6 | 4.984 | 9.774 | 5.145 | 9.871 | 5.419 | 9.984 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 181.6 | 181.3 | 180.7 | 180.1 | 180.9 | 179.7 | 181.2 | 181 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.6 | 181.3 | 180.7 | 180.1 | 180.9 | 179.7 | 181.2 | 181 |
| CPU used with Omni's own (cores), mean | 2.129 | 2.11 | 2.007 | 2.022 | 2.003 | 2.01 | 2.071 | 2.077 |
| host CPU busy, the real machine under kind (%) | 62.88 | 62.73 | 59.58 | 60.1 | 59.39 | 59.6 | 61.25 | 61.93 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1555 | 1420 | -8.7% | -298.3 to +28.36 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5235 | 5131 | -2.0% | -478.7 to +271.6 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 24.28 | 16.13 | -33.6% | -9.91 to -6.401 | GAIN |
| failed requests (%) | 9.999 | 7.979 | -20.2% | -2.853 to -1.186 | GAIN |
| HPA replicas, mean | 9.649 | 12.88 | +33.5% | +2.827 to +3.635 | power given |
| pods started | 5.323 | 10.6 | +99.1% | +4.768 to +5.78 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.445e-16 to +1.726e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.6 | 181.3 | -0.2% | -0.6003 to +0.01579 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.6 | 181.3 | -0.2% | -0.6003 to +0.01579 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.129 | 2.11 | -0.9% | -0.03106 to -0.008091 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.88 | 62.73 | -0.2% | -0.4391 to +0.1409 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.617e+05 to +8.622e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.146e-05 to -8.142e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1814 | 1791 | -1.2% | -293.5 to +248.4 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5368 | 5532 | +3.1% | -100.1 to +428.8 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 19.38 | 14.51 | -25.1% | -5.871 to -3.87 | GAIN |
| failed requests (%) | 6.466 | 5.948 | -8.0% | -0.9483 to -0.08818 | GAIN |
| HPA replicas, mean | 9.625 | 13.45 | +39.8% | +3.302 to +4.356 | power given |
| pods started | 4.984 | 9.774 | +96.1% | +4.175 to +5.405 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.4e-16 to +9.616e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 180.1 | -0.4% | -0.9574 to -0.3294 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 180.1 | -0.4% | -0.9574 to -0.3294 | GAIN |
| CPU used with Omni's own (cores), mean | 2.007 | 2.022 | +0.7% | +0.006325 to +0.02293 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.58 | 60.1 | +0.9% | +0.28 to +0.7599 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1776 | 1869 | +5.2% | -117.4 to +302.3 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5599 | 5407 | -3.4% | -504.2 to +118.8 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 19.89 | 14.33 | -27.9% | -6.525 to -4.583 | GAIN |
| failed requests (%) | 6.685 | 5.761 | -13.8% | -1.302 to -0.5447 | GAIN |
| HPA replicas, mean | 9.621 | 13.47 | +40.0% | +3.354 to +4.348 | power given |
| pods started | 5.145 | 9.871 | +91.8% | +4.068 to +5.384 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.853e-16 to +2.692e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 179.7 | -0.6% | -1.47 to -0.7961 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 179.7 | -0.6% | -1.47 to -0.7961 | GAIN |
| CPU used with Omni's own (cores), mean | 2.003 | 2.01 | +0.4% | -0.000456 to +0.01602 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.39 | 59.6 | +0.4% | +0.00895 to +0.4119 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1597 | 1408 | -11.8% | -340.4 to -37.22 | GAIN |
| response time (ms), 99th percentile | 4357 | 4526 | +3.9% | -167 to +505.5 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 23.05 | 16.75 | -27.3% | -7.499 to -5.102 | GAIN |
| failed requests (%) | 7.045 | 6.621 | -6.0% | -0.6725 to -0.1747 | GAIN |
| HPA replicas, mean | 9.578 | 13.41 | +40.0% | +3.351 to +4.314 | power given |
| pods started | 5.419 | 9.984 | +84.2% | +3.971 to +5.158 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.017e-16 to -5.728e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.2 | 181 | -0.1% | -0.4945 to +0.1417 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.2 | 181 | -0.1% | -0.4945 to +0.1417 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.071 | 2.077 | +0.3% | -0.001052 to +0.01202 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.25 | 61.93 | +1.1% | +0.5242 to +0.8384 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
