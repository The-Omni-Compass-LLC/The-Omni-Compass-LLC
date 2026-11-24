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
| response time (ms), 95th percentile | 3002 | 3558 | 2295 | 3168 | 2698 | 4102 | 2349 | 3405 | 2489 | 3313 | 3317 | 3238 | 2344 | 3638 |
| response time (ms), 99th percentile | 5564 | 6252 | 4425 | 5883 | 5999 | 7033 | 5202 | 6247 | 5390 | 5662 | 5719 | 5797 | 4353 | 5838 |
| time over the response line (% of samples) | 41.25 | 39.4 | 39.44 | 36.99 | 44.02 | 42.36 | 41.35 | 40.1 | 40.48 | 38 | 45.7 | 42.05 | 41.95 | 44.25 |
| failed requests (%) | 25.16 | 25.1 | 19.61 | 20.54 | 27.68 | 27.65 | 25.48 | 25.36 | 22.54 | 22.99 | 26.3 | 25.97 | 20.51 | 25.78 |
| HPA replicas, mean | 9.635 | 14.45 | 9.669 | 13.48 | 9.654 | 14.47 | 9.635 | 14.24 | 9.64 | 13.46 | 9.662 | 12.48 | 9.693 | 12.57 |
| pods started | 5 | 11.14 | 4.886 | 10.46 | 4.886 | 10.83 | 5 | 10.74 | 5.2 | 11.54 | 4.914 | 9.686 | 4.486 | 9 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184 | 184.1 | 184.5 | 184.8 | 184.5 | 184.3 | 184.2 | 183.6 | 184 | 184.7 | 184 | 184.4 | 184.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184 | 184.1 | 184.5 | 184.8 | 184.5 | 184.3 | 184.2 | 183.6 | 184 | 184.7 | 184 | 184.4 | 184.3 |
| CPU used with Omni's own (cores), mean | 2.379 | 2.426 | 2.399 | 2.452 | 2.419 | 2.469 | 2.384 | 2.446 | 2.334 | 2.389 | 2.397 | 2.441 | 2.4 | 2.453 |
| host CPU busy, the real machine under kind (%) | 70.24 | 72.21 | 70.6 | 73.17 | 71.83 | 74 | 70.86 | 73.44 | 68.6 | 71.15 | 71.62 | 74.34 | 72.1 | 76.53 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.002857 | 0 | 0.01429 | 0.04571 | 0.005714 | 0.005714 | 0.005714 | 0.01143 | 0.005714 | 0.01714 | 0.09714 | 0.1029 | 0.1743 | 0.1886 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3002 | 3558 | +18.6% | -149.6 to +1264 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5564 | 6252 | +12.4% | +66.24 to +1310 | LOSS |
| time over the response line (% of samples) | 41.25 | 39.4 | -4.5% | -2.82 to -0.8783 | GAIN |
| failed requests (%) | 25.16 | 25.1 | -0.2% | -1.475 to +1.363 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.635 | 14.45 | +50.0% | +4.599 to +5.039 | power given |
| pods started | 5 | 11.14 | +122.9% | +5.536 to +6.75 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.962e-16 to +1.379e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184 | -0.1% | -0.652 to +0.3623 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184 | -0.1% | -0.652 to +0.3623 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.379 | 2.426 | +2.0% | +0.03774 to +0.05594 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.24 | 72.21 | +2.8% | +1.704 to +2.235 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0.002857 | 0 | -100.0% | -0.008663 to +0.002949 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2295 | 3168 | +38.0% | +295.7 to +1450 | LOSS |
| response time (ms), 99th percentile | 4425 | 5883 | +32.9% | +609.1 to +2306 | LOSS |
| time over the response line (% of samples) | 39.44 | 36.99 | -6.2% | -4.215 to -0.6751 | GAIN |
| failed requests (%) | 19.61 | 20.54 | +4.7% | -0.5112 to +2.367 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.669 | 13.48 | +39.4% | +3.19 to +4.437 | power given |
| pods started | 4.886 | 10.46 | +114.0% | +4.883 to +6.26 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.112e-15 to -2.077e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.5 | +0.3% | -0.009922 to +0.9499 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.5 | +0.3% | -0.009922 to +0.9499 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.399 | 2.452 | +2.2% | +0.04232 to +0.06473 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.6 | 73.17 | +3.6% | +2.206 to +2.921 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01429 | 0.04571 | +220.0% | +0.009751 to +0.05311 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2698 | 4102 | +52.1% | +627.5 to +2181 | LOSS |
| response time (ms), 99th percentile | 5999 | 7033 | +17.2% | +255.2 to +1813 | LOSS |
| time over the response line (% of samples) | 44.02 | 42.36 | -3.8% | -2.875 to -0.4458 | GAIN |
| failed requests (%) | 27.68 | 27.65 | -0.1% | -1.331 to +1.263 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.654 | 14.47 | +49.9% | +4.563 to +5.07 | power given |
| pods started | 4.886 | 10.83 | +121.6% | +5.366 to +6.52 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.274e-16 to +2.184e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.8 | 184.5 | -0.1% | -0.7626 to +0.2354 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.8 | 184.5 | -0.1% | -0.7626 to +0.2354 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.419 | 2.469 | +2.1% | +0.03929 to +0.0615 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.83 | 74 | +3.0% | +1.959 to +2.372 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.005714 | 0.005714 | +0.0% | -0.01178 to +0.01178 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2349 | 3405 | +44.9% | +245.4 to +1865 | LOSS |
| response time (ms), 99th percentile | 5202 | 6247 | +20.1% | +343.7 to +1746 | LOSS |
| time over the response line (% of samples) | 41.35 | 40.1 | -3.0% | -2.53 to +0.03935 | STEADY, inside the noise (cut) |
| failed requests (%) | 25.48 | 25.36 | -0.5% | -1.351 to +1.106 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.635 | 14.24 | +47.8% | +4.323 to +4.882 | power given |
| pods started | 5 | 10.74 | +114.9% | +5.029 to +6.456 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.983e-16 to +2.416e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.2 | -0.1% | -0.5541 to +0.355 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.2 | -0.1% | -0.5541 to +0.355 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.384 | 2.446 | +2.6% | +0.04873 to +0.07521 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.86 | 73.44 | +3.6% | +2.206 to +2.959 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.005714 | 0.01143 | +100.0% | -0.008576 to +0.02 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2489 | 3313 | +33.1% | +243.9 to +1405 | LOSS |
| response time (ms), 99th percentile | 5390 | 5662 | +5.0% | -441.8 to +985.7 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 40.48 | 38 | -6.1% | -3.987 to -0.9797 | GAIN |
| failed requests (%) | 22.54 | 22.99 | +2.0% | -0.5606 to +1.452 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.64 | 13.46 | +39.7% | +3.258 to +4.386 | power given |
| pods started | 5.2 | 11.54 | +122.0% | +5.687 to +6.998 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.147e-15 to -2.741e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 184 | +0.2% | -0.1762 to +0.8658 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.6 | 184 | +0.2% | -0.1762 to +0.8658 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.334 | 2.389 | +2.4% | +0.04589 to +0.06384 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.6 | 71.15 | +3.7% | +2.261 to +2.831 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.005714 | 0.01714 | +200.0% | -0.004749 to +0.02761 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3317 | 3238 | -2.4% | -710.2 to +551.9 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5719 | 5797 | +1.4% | -624.9 to +780.8 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 45.7 | 42.05 | -8.0% | -5.153 to -2.137 | GAIN |
| failed requests (%) | 26.3 | 25.97 | -1.2% | -2.579 to +1.926 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.662 | 12.48 | +29.2% | +2.162 to +3.478 | power given |
| pods started | 4.914 | 9.686 | +97.1% | +3.985 to +5.558 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.242e-16 to +8.84e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 184 | -0.4% | -1.107 to -0.3066 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 184 | -0.4% | -1.107 to -0.3066 | GAIN |
| CPU used with Omni's own (cores), mean | 2.397 | 2.441 | +1.8% | +0.03347 to +0.05318 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.62 | 74.34 | +3.8% | +2.388 to +3.053 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.09714 | 0.1029 | +5.9% | -0.002375 to +0.0138 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2344 | 3638 | +55.3% | +786.5 to +1803 | LOSS |
| response time (ms), 99th percentile | 4353 | 5838 | +34.1% | +808.3 to +2162 | LOSS |
| time over the response line (% of samples) | 41.95 | 44.25 | +5.5% | +0.1113 to +4.493 | LOSS |
| failed requests (%) | 20.51 | 25.78 | +25.7% | +3.486 to +7.053 | LOSS |
| HPA replicas, mean | 9.693 | 12.57 | +29.7% | +2.078 to +3.685 | power given |
| pods started | 4.486 | 9 | +100.6% | +3.534 to +5.494 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.352e-16 to +6.413e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.3 | -0.0% | -0.597 to +0.4309 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.3 | -0.0% | -0.597 to +0.4309 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.4 | 2.453 | +2.2% | +0.03376 to +0.07225 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.1 | 76.53 | +6.2% | +3.816 to +5.054 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1743 | 0.1886 | +8.2% | -0.0109 to +0.03947 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
