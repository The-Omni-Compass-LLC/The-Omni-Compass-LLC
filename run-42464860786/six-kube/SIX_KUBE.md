# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3690 | 5081 | 2401 | 3192 | 2174 | 1347 | 2042 | 3590 | 2299 | 2918 | 2697 | 3857 | 2783 | 3180 |
| response time (ms), 99th percentile | 6360 | 7845 | 3905 | 5864 | 3341 | 3761 | 3460 | 4684 | 5367 | 4986 | 5119 | 6060 | 4522 | 5598 |
| time over the response line (% of samples) | 47.75 | 46.1 | 31.43 | 30.97 | 29.44 | 27.03 | 31.74 | 31.88 | 48.91 | 36.89 | 52.21 | 55.44 | 38.62 | 38.24 |
| failed requests (%) | 27.4 | 30.82 | 13.52 | 13.79 | 19.35 | 20.19 | 20.42 | 21.53 | 31.19 | 25.62 | 34.25 | 37.93 | 17.52 | 19.11 |
| HPA replicas, mean | 9.675 | 14.2 | 9.629 | 14.42 | 9.59 | 13.77 | 9.636 | 14.3 | 9.655 | 13.08 | 9.715 | 11.89 | 9.688 | 12.55 |
| pods started | 4.5 | 9.6 | 5.143 | 11.86 | 5.5 | 12.38 | 4.286 | 10.57 | 5 | 10.67 | 4.375 | 8.857 | 4.25 | 9.625 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 185.9 | 186.1 | 183.4 | 183.8 | 181.2 | 182.1 | 181.7 | 182.7 | 184.1 | 183.2 | 185.2 | 186.5 | 183.4 | 184.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.9 | 186.1 | 183.4 | 183.8 | 181.2 | 182.1 | 181.7 | 182.7 | 184.1 | 183.2 | 185.2 | 186.5 | 183.4 | 184.3 |
| CPU used with Omni's own (cores), mean | 2.518 | 2.57 | 2.271 | 2.33 | 2.124 | 2.129 | 2.145 | 2.182 | 2.389 | 2.304 | 2.455 | 2.618 | 2.336 | 2.373 |
| host CPU busy, the real machine under kind (%) | 73.79 | 76.14 | 66.58 | 69.13 | 62.6 | 63.6 | 63.51 | 65.23 | 69.95 | 68.47 | 72.75 | 78.77 | 69.54 | 73.19 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.01429 | 0 | 0.0125 | 0.0125 | 0 | 0.04286 | 0 | 0 | 0.1 | 0.2 | 0.1375 | 0.175 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

4 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3690 | 4940 | +33.9% | -3097 to +5597 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6360 | 7885 | +24.0% | -3033 to +6083 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 47.75 | 43.8 | -8.3% | -8.762 to +0.8711 | STEADY, inside the noise (cut) |
| failed requests (%) | 27.4 | 28.23 | +3.0% | -2.233 to +3.9 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.675 | 14.38 | +48.6% | +3.466 to +5.947 | power given |
| pods started | 4.5 | 10 | +122.2% | +3.446 to +7.554 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2e-15 to +1.556e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.9 | 185.8 | -0.1% | -2.511 to +2.279 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.9 | 185.8 | -0.1% | -2.511 to +2.279 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.518 | 2.559 | +1.7% | +0.02128 to +0.06211 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.79 | 75.58 | +2.4% | +1.441 to +2.144 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008375 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

7 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2401 | 3192 | +32.9% | -66.99 to +1648 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3905 | 5864 | +50.2% | -427.7 to +4347 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 31.43 | 30.97 | -1.5% | -5.511 to +4.588 | STEADY, inside the noise (cut) |
| failed requests (%) | 13.52 | 13.79 | +2.0% | -1.489 to +2.024 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.629 | 14.42 | +49.7% | +3.934 to +5.646 | power given |
| pods started | 5.143 | 11.86 | +130.6% | +4.887 to +8.542 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.471e-16 to +6.546e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 183.8 | +0.3% | -1.003 to +1.952 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 183.8 | +0.3% | -1.003 to +1.952 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.271 | 2.33 | +2.6% | +0.01481 to +0.1037 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.58 | 69.13 | +3.8% | +0.8696 to +4.236 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01429 | 0 | -100.0% | -0.04924 to +0.02067 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2174 | 1347 | -38.0% | -1951 to +296.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3341 | 3761 | +12.6% | -405.6 to +1246 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 29.44 | 27.03 | -8.2% | -4.192 to -0.6242 | GAIN |
| failed requests (%) | 19.35 | 20.19 | +4.3% | -0.504 to +2.175 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.59 | 13.77 | +43.6% | +3.343 to +5.023 | power given |
| pods started | 5.5 | 12.38 | +125.0% | +5.502 to +8.248 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.031e-16 to +7.472e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.2 | 182.1 | +0.5% | -0.6441 to +2.385 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.2 | 182.1 | +0.5% | -0.6441 to +2.385 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.124 | 2.129 | +0.2% | -0.04347 to +0.05326 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.6 | 63.6 | +1.6% | -0.3086 to +2.311 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.0125 | 0.0125 | +0.0% | -0.04469 to +0.04469 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

7 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2042 | 3590 | +75.8% | -389.7 to +3485 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3460 | 4684 | +35.4% | -472.3 to +2922 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 31.74 | 31.88 | +0.5% | -1.907 to +2.199 | STEADY, inside the noise (up) |
| failed requests (%) | 20.42 | 21.53 | +5.4% | -1.865 to +4.085 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.636 | 14.3 | +48.4% | +4.188 to +5.138 | power given |
| pods started | 4.286 | 10.57 | +146.7% | +5.834 to +6.737 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.937e-16 to +4.4e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.7 | 182.7 | +0.5% | -0.5087 to +2.472 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.7 | 182.7 | +0.5% | -0.5087 to +2.472 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.145 | 2.182 | +1.7% | +0.01133 to +0.06217 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.51 | 65.23 | +2.7% | +1.248 to +2.201 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0 | 0.04286 | +0.0429 | -0.00658 to +0.09229 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (organism energy (J); organism work per energy), STEADY (inside the noise) on 8

4 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2204 | 3072 | +39.4% | -1382 to +3117 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4572 | 5713 | +24.9% | -380.7 to +2662 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 44.42 | 39 | -12.2% | -11.03 to +0.184 | STEADY, inside the noise (cut) |
| failed requests (%) | 27.12 | 26.98 | -0.5% | -4.796 to +4.517 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.64 | 12.89 | +33.7% | -0.516 to +7.015 | STEADY, inside the noise (up) |
| pods started | 5.25 | 10.5 | +100.0% | -0.468 to +10.97 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.632e-15 to +1.632e-15 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 184.1 | +0.2% | -1.347 to +1.997 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 184.1 | +0.2% | -1.347 to +1.997 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.327 | 2.373 | +2.0% | +0.0304 to +0.06119 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.14 | 70.15 | +3.0% | +1.606 to +2.415 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

7 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3044 | 3857 | +26.7% | -2211 to +3837 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5790 | 6060 | +4.7% | -2499 to +3039 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 59.6 | 55.44 | -7.0% | -7.08 to -1.249 | GAIN |
| failed requests (%) | 39.15 | 37.93 | -3.1% | -5.422 to +2.994 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.747 | 11.89 | +22.0% | +0.2271 to +4.064 | power given |
| pods started | 4 | 8.857 | +121.4% | +3.613 to +6.101 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.469e-16 to +1.416e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.3 | 186.5 | +0.1% | -1.258 to +1.694 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.3 | 186.5 | +0.1% | -1.258 to +1.694 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.576 | 2.618 | +1.6% | +0.01678 to +0.06695 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.2 | 78.77 | +3.4% | +2.201 to +2.942 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1 | 0.2 | +100.0% | +0.1 to +0.1 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2783 | 3180 | +14.3% | -98.97 to +892.5 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4522 | 5598 | +23.8% | -375.1 to +2528 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 38.62 | 38.24 | -1.0% | -3.642 to +2.894 | STEADY, inside the noise (cut) |
| failed requests (%) | 17.52 | 19.11 | +9.1% | -1.435 to +4.617 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.688 | 12.55 | +29.5% | +0.7789 to +4.938 | power given |
| pods started | 4.25 | 9.625 | +126.5% | +3.966 to +6.784 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.674e-15 to +5.633e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 184.3 | +0.5% | -0.2698 to +2.016 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 184.3 | +0.5% | -0.2698 to +2.016 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.336 | 2.373 | +1.6% | +0.01645 to +0.05853 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.54 | 73.19 | +5.2% | +2.86 to +4.441 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1375 | 0.175 | +27.3% | -0.005775 to +0.08078 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
