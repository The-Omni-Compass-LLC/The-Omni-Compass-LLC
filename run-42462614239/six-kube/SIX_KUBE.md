# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on: native | The spine, the muscles every stack runs on: omni | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1001 | 781.4 | 1290 | 1461 | 1710 | 1618 | 1832 | 1346 | 1252 | 1313 | 1779 | 1761 | 1161 | 1318 |
| response time (ms), 99th percentile | 3110 | 3162 | 3915 | 4741 | 5601 | 5604 | 5930 | 5633 | 3159 | 3475 | 4453 | 4197 | 3719 | 4086 |
| time over the response line (% of samples) | 10.74 | 7.373 | 25.92 | 20.01 | 18.9 | 14.04 | 18.16 | 12.67 | 18.23 | 13.49 | 23.38 | 18.34 | 20.53 | 16.56 |
| failed requests (%) | 1.934 | 2.349 | 12.39 | 10.68 | 6.195 | 5.734 | 5.516 | 5.039 | 5.61 | 4.989 | 10.19 | 7.726 | 8.952 | 8.366 |
| HPA replicas, mean | 9.446 | 13.96 | 9.639 | 14.39 | 9.646 | 14.21 | 9.593 | 14.23 | 9.559 | 13.59 | 9.594 | 14.13 | 9.607 | 14.2 |
| pods started | 6.5 | 12.75 | 5 | 11.9 | 4.444 | 10.11 | 5.375 | 11.33 | 5.222 | 10.89 | 4.875 | 12 | 5.375 | 12.38 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 176.2 | 176 | 182.1 | 181.7 | 180 | 180.2 | 179.8 | 180.5 | 180 | 179.2 | 180.6 | 179.5 | 180.2 | 179.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 176.2 | 176 | 182.1 | 181.7 | 180 | 180.2 | 179.8 | 180.5 | 180 | 179.2 | 180.6 | 179.5 | 180.2 | 179.8 |
| CPU used with Omni's own (cores), mean | 1.592 | 1.671 | 2.13 | 2.182 | 1.981 | 2.018 | 1.992 | 2.014 | 1.905 | 1.929 | 1.963 | 1.98 | 1.959 | 2.001 |
| host CPU busy, the real machine under kind (%) | 47.95 | 50.35 | 63.27 | 65.05 | 58.81 | 60.09 | 59.05 | 59.69 | 57.24 | 58.06 | 58.69 | 59.46 | 58.3 | 60.26 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0875 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

4 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1001 | 781.4 | -21.9% | -473.7 to +35.12 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3110 | 3162 | +1.7% | -1402 to +1506 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 10.74 | 7.373 | -31.3% | -9.579 to +2.852 | STEADY, inside the noise (cut) |
| failed requests (%) | 1.934 | 2.349 | +21.4% | -0.4426 to +1.272 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.446 | 13.96 | +47.8% | +2.351 to +6.678 | power given |
| pods started | 6.5 | 12.75 | +96.2% | +2.97 to +9.53 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.131e-15 to +1.575e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 176.2 | 176 | -0.1% | -2.596 to +2.196 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 176.2 | 176 | -0.1% | -2.596 to +2.196 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.592 | 1.671 | +5.0% | +0.01765 to +0.1407 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 47.95 | 50.35 | +5.0% | -0.1561 to +4.957 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.91e+05 to +8.162e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.611e-05 to -9.314e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1290 | 1461 | +13.3% | -311.7 to +654.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3915 | 4741 | +21.1% | -619 to +2271 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 25.92 | 20.01 | -22.8% | -9.181 to -2.651 | GAIN |
| failed requests (%) | 12.39 | 10.68 | -13.8% | -3.279 to -0.1311 | GAIN |
| HPA replicas, mean | 9.639 | 14.39 | +49.2% | +4.407 to +5.085 | power given |
| pods started | 5 | 11.9 | +138.0% | +5.92 to +7.88 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.286e-16 to +9.063e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.1 | 181.7 | -0.2% | -1.382 to +0.5916 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.1 | 181.7 | -0.2% | -1.382 to +0.5916 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.13 | 2.182 | +2.4% | +0.02808 to +0.07591 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.27 | 65.05 | +2.8% | +1.195 to +2.36 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.623e+05 to +8.632e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.156e-05 to -8.147e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

9 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1710 | 1618 | -5.3% | -839.3 to +656.7 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5601 | 5604 | +0.0% | -609.9 to +615.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 18.9 | 14.04 | -25.7% | -7.966 to -1.758 | GAIN |
| failed requests (%) | 6.195 | 5.734 | -7.4% | -1.1 to +0.1777 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.646 | 14.21 | +47.3% | +3.526 to +5.606 | power given |
| pods started | 4.444 | 10.11 | +127.5% | +4.129 to +7.204 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.191e-15 to +2.173e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180 | 180.2 | +0.1% | -0.6887 to +1.079 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180 | 180.2 | +0.1% | -0.6887 to +1.079 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.981 | 2.018 | +1.9% | +0.01463 to +0.05914 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.81 | 60.09 | +2.2% | +0.8178 to +1.738 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

6 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1803 | 1346 | -25.4% | -1330 to +416.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5718 | 5633 | -1.5% | -801.1 to +631.3 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 17.8 | 12.67 | -28.8% | -8.64 to -1.614 | GAIN |
| failed requests (%) | 5.592 | 5.039 | -9.9% | -1.654 to +0.5483 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.558 | 14.23 | +48.9% | +3.51 to +5.835 | power given |
| pods started | 5.667 | 11.33 | +100.0% | +4.086 to +7.247 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.387e-15 to +1.091e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.4 | 180.5 | +0.6% | +0.5839 to +1.562 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.4 | 180.5 | +0.6% | +0.5839 to +1.562 | power given |
| CPU used with Omni's own (cores), mean | 1.959 | 2.014 | +2.8% | +0.0269 to +0.08279 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.14 | 59.69 | +2.7% | +0.7278 to +2.368 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

9 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1252 | 1313 | +4.8% | -126.9 to +248 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3159 | 3475 | +10.0% | -204.1 to +835.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 18.23 | 13.49 | -26.0% | -8.248 to -1.223 | GAIN |
| failed requests (%) | 5.61 | 4.989 | -11.1% | -1.157 to -0.08579 | GAIN |
| HPA replicas, mean | 9.559 | 13.59 | +42.2% | +2.595 to +5.467 | power given |
| pods started | 5.222 | 10.89 | +108.5% | +3.784 to +7.55 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.404e-15 to +4.169e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180 | 179.2 | -0.5% | -1.89 to +0.1417 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180 | 179.2 | -0.5% | -1.89 to +0.1417 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.905 | 1.929 | +1.3% | -0.01681 to +0.06512 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.24 | 58.06 | +1.4% | -0.9376 to +2.566 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.377e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1779 | 1761 | -1.0% | -694.3 to +659.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4453 | 4197 | -5.7% | -855.2 to +343.3 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 23.38 | 18.34 | -21.5% | -11.85 to +1.782 | STEADY, inside the noise (cut) |
| failed requests (%) | 10.19 | 7.726 | -24.2% | -5.026 to +0.09573 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.594 | 14.13 | +47.3% | +3.799 to +5.269 | power given |
| pods started | 4.875 | 12 | +146.2% | +5.427 to +8.823 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.49e-16 to +1.215e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 179.5 | -0.6% | -2.076 to -0.03088 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 179.5 | -0.6% | -2.076 to -0.03088 | GAIN |
| CPU used with Omni's own (cores), mean | 1.963 | 1.98 | +0.9% | -0.02529 to +0.06018 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.69 | 59.46 | +1.3% | -0.1736 to +1.713 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1161 | 1318 | +13.5% | -390.1 to +703 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3719 | 4086 | +9.9% | -925.1 to +1658 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 20.53 | 16.56 | -19.3% | -7.382 to -0.5394 | GAIN |
| failed requests (%) | 8.952 | 8.366 | -6.5% | -1.924 to +0.7526 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.607 | 14.2 | +47.8% | +3.808 to +5.377 | power given |
| pods started | 5.375 | 12.38 | +130.2% | +5.157 to +8.843 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.41e-16 to +1.191e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.2 | 179.8 | -0.3% | -1.89 to +0.9263 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.2 | 179.8 | -0.3% | -1.89 to +0.9263 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.959 | 2.001 | +2.1% | +0.00108 to +0.08278 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.3 | 60.26 | +3.4% | +0.7981 to +3.121 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4.001e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.987e-09 to -4.984e-09 | power given |
| organism behind its window (s) | 0 | 0.0875 | +0.0875 | +0.05794 to +0.1171 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
