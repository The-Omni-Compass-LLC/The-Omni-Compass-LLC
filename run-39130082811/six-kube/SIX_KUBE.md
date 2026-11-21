# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on: native | The spine, the muscles every stack runs on: omni | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1703 | 1647 | 1205 | 1105 | 1618 | 1515 | 1927 | 1796 | 1921 | 1922 | 1559 | 1418 | 1634 | 1600 |
| response time (ms), 99th percentile | 5314 | 5126 | 3560 | 3936 | 4359 | 4492 | 5754 | 5768 | 5646 | 5579 | 4283 | 4267 | 4877 | 5620 |
| time over the response line (% of samples) | 18.87 | 13.91 | 18.91 | 13.08 | 16.48 | 12.75 | 22.29 | 16.63 | 31.6 | 22.8 | 24.87 | 18.23 | 28.68 | 20.56 |
| failed requests (%) | 6.337 | 5.752 | 8.113 | 6.398 | 5.788 | 5.048 | 7.845 | 7.279 | 10.42 | 9.441 | 9.969 | 8.211 | 12.71 | 10.35 |
| HPA replicas, mean | 9.59 | 13.21 | 9.599 | 12.23 | 9.568 | 12.82 | 9.639 | 13.77 | 9.677 | 14.24 | 9.582 | 12.61 | 9.675 | 13.4 |
| pods started | 5.371 | 9.4 | 5.571 | 9.914 | 5.343 | 9.286 | 5 | 9.6 | 4.6 | 9.743 | 5.314 | 10.11 | 5.057 | 10.26 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 179.7 | 179.8 | 179.6 | 179.3 | 178.4 | 181.4 | 180.5 | 183.5 | 182.9 | 180.8 | 180.7 | 182.4 | 182.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 179.7 | 179.8 | 179.6 | 179.3 | 178.4 | 181.4 | 180.5 | 183.5 | 182.9 | 180.8 | 180.7 | 182.4 | 182.5 |
| CPU used with Omni's own (cores), mean | 1.965 | 1.969 | 1.944 | 1.938 | 1.877 | 1.885 | 2.067 | 2.073 | 2.283 | 2.282 | 2.052 | 2.044 | 2.214 | 2.211 |
| host CPU busy, the real machine under kind (%) | 58.22 | 58.31 | 57.83 | 57.94 | 55.9 | 56.13 | 61.21 | 61.58 | 67.1 | 67.68 | 60.8 | 60.97 | 65.75 | 66.05 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.08571 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1703 | 1647 | -3.3% | -295 to +181.3 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5314 | 5126 | -3.5% | -425.7 to +49.39 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 18.87 | 13.91 | -26.3% | -6.284 to -3.647 | GAIN |
| failed requests (%) | 6.337 | 5.752 | -9.2% | -1.009 to -0.1628 | GAIN |
| HPA replicas, mean | 9.59 | 13.21 | +37.7% | +2.839 to +4.393 | power given |
| pods started | 5.371 | 9.4 | +75.0% | +3.232 to +4.825 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.407e-16 to +3.915e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 179.7 | -0.4% | -1.182 to -0.2872 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 179.7 | -0.4% | -1.182 to -0.2872 | GAIN |
| CPU used with Omni's own (cores), mean | 1.965 | 1.969 | +0.2% | -0.005572 to +0.01299 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.22 | 58.31 | +0.2% | -0.1063 to +0.2947 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.97e+05 to +7.989e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.408e-05 to -9.385e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1205 | 1105 | -8.3% | -198.5 to -1.438 | GAIN |
| response time (ms), 99th percentile | 3560 | 3936 | +10.6% | -17.12 to +768.4 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 18.91 | 13.08 | -30.9% | -7.967 to -3.705 | GAIN |
| failed requests (%) | 8.113 | 6.398 | -21.1% | -2.702 to -0.7275 | GAIN |
| HPA replicas, mean | 9.599 | 12.23 | +27.4% | +1.899 to +3.36 | power given |
| pods started | 5.571 | 9.914 | +77.9% | +3.473 to +5.212 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.164e-16 to +5.807e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 179.6 | -0.1% | -0.5867 to +0.2208 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 179.6 | -0.1% | -0.5867 to +0.2208 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.944 | 1.938 | -0.3% | -0.01731 to +0.006907 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.83 | 57.94 | +0.2% | -0.2187 to +0.435 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.62e+05 to +8.624e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.149e-05 to -8.145e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1618 | 1515 | -6.3% | -371.8 to +166.6 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4359 | 4492 | +3.0% | -357.5 to +622.7 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 16.48 | 12.75 | -22.6% | -5.017 to -2.444 | GAIN |
| failed requests (%) | 5.788 | 5.048 | -12.8% | -1.226 to -0.2537 | GAIN |
| HPA replicas, mean | 9.568 | 12.82 | +34.0% | +2.441 to +4.055 | power given |
| pods started | 5.343 | 9.286 | +73.8% | +2.923 to +4.963 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.554e-16 to +4.062e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.3 | 178.4 | -0.5% | -1.296 to -0.5073 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.3 | 178.4 | -0.5% | -1.296 to -0.5073 | GAIN |
| CPU used with Omni's own (cores), mean | 1.877 | 1.885 | +0.4% | -0.007365 to +0.02269 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.9 | 56.13 | +0.4% | -0.1445 to +0.6129 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1927 | 1796 | -6.8% | -443.5 to +180.8 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5754 | 5768 | +0.2% | -485.2 to +512.6 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 22.29 | 16.63 | -25.4% | -6.875 to -4.436 | GAIN |
| failed requests (%) | 7.845 | 7.279 | -7.2% | -0.8602 to -0.2717 | GAIN |
| HPA replicas, mean | 9.639 | 13.77 | +42.8% | +3.438 to +4.82 | power given |
| pods started | 5 | 9.6 | +92.0% | +3.774 to +5.426 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.509e-16 to -6.268e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 180.5 | -0.5% | -1.282 to -0.4567 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 180.5 | -0.5% | -1.282 to -0.4567 | GAIN |
| CPU used with Omni's own (cores), mean | 2.067 | 2.073 | +0.3% | -0.002166 to +0.01493 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.21 | 61.58 | +0.6% | +0.1911 to +0.5465 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1921 | 1922 | +0.1% | -260.1 to +263.3 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5646 | 5579 | -1.2% | -515.6 to +382.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 31.6 | 22.8 | -27.9% | -10.64 to -6.967 | GAIN |
| failed requests (%) | 10.42 | 9.441 | -9.4% | -1.504 to -0.4626 | GAIN |
| HPA replicas, mean | 9.677 | 14.24 | +47.2% | +4.052 to +5.076 | power given |
| pods started | 4.6 | 9.743 | +111.8% | +4.406 to +5.879 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.151e-16 to +1.598e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 182.9 | -0.3% | -1.089 to -0.07908 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 182.9 | -0.3% | -1.089 to -0.07908 | GAIN |
| CPU used with Omni's own (cores), mean | 2.283 | 2.282 | -0.1% | -0.01263 to +0.009918 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.1 | 67.68 | +0.9% | +0.3161 to +0.8533 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1559 | 1418 | -9.0% | -282.9 to +2.538 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4283 | 4267 | -0.4% | -481.5 to +450 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 24.87 | 18.23 | -26.7% | -8.534 to -4.736 | GAIN |
| failed requests (%) | 9.969 | 8.211 | -17.6% | -2.787 to -0.7282 | GAIN |
| HPA replicas, mean | 9.582 | 12.61 | +31.6% | +2.258 to +3.799 | power given |
| pods started | 5.314 | 10.11 | +90.3% | +3.947 to +5.653 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.221e-16 to +2.191e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 180.7 | -0.1% | -0.4578 to +0.2257 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 180.7 | -0.1% | -0.4578 to +0.2257 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.052 | 2.044 | -0.3% | -0.01578 to +0.001487 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.8 | 60.97 | +0.3% | -0.07678 to +0.4125 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1634 | 1600 | -2.1% | -222.3 to +154.6 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4877 | 5620 | +15.2% | +267.6 to +1218 | LOSS |
| time over the response line (% of samples) | 28.68 | 20.56 | -28.3% | -10.22 to -6.016 | GAIN |
| failed requests (%) | 12.71 | 10.35 | -18.6% | -3.259 to -1.471 | GAIN |
| HPA replicas, mean | 9.675 | 13.4 | +38.5% | +3.187 to +4.271 | power given |
| pods started | 5.057 | 10.26 | +102.8% | +4.535 to +5.865 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.541e-16 to +4.556e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.4 | 182.5 | +0.1% | -0.3097 to +0.562 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.4 | 182.5 | +0.1% | -0.3097 to +0.562 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.214 | 2.211 | -0.1% | -0.01426 to +0.009803 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.75 | 66.05 | +0.5% | -0.08782 to +0.6948 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.08571 | +0.0857 | +0.07352 to +0.09791 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
