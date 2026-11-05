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
| response time (ms), 95th percentile | 3966 | 3148 | 4534 | 3768 | 3872 | 2659 | 4334 | 3418 | 3808 | 3358 |
| response time (ms), 99th percentile | 5915 | 5202 | 6707 | 6194 | 6235 | 5284 | 6531 | 6188 | 5936 | 5675 |
| time over the response line (% of samples) | 48.48 | 49.47 | 58.05 | 59.93 | 54.73 | 53.15 | 61.04 | 59.48 | 53.27 | 53.02 |
| failed requests (%) | 32.23 | 36.26 | 41.86 | 44.42 | 39.05 | 43.21 | 43.58 | 47.78 | 39.98 | 40.94 |
| HPA replicas, mean | 9.787 | 12.29 | 9.818 | 11.32 | 9.8 | 11.51 | 9.83 | 11.05 | 9.806 | 11.91 |
| pods started | 4.42 | 9.98 | 3.9 | 6.5 | 4.2 | 9.14 | 3.82 | 7.28 | 4.08 | 7.878 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.2 | 276 | 277.7 | 277.7 | 276.3 | 276.2 | 277.8 | 277 | 276.6 | 277.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.2 | 276 | 277.7 | 277.7 | 276.3 | 276.2 | 277.8 | 277 | 276.6 | 277.2 |
| CPU used with Omni's own (cores), mean | 2.408 | 2.453 | 2.507 | 2.551 | 2.416 | 2.457 | 2.499 | 2.536 | 2.454 | 2.502 |
| host CPU busy, the real machine under kind (%) | 70.97 | 75.49 | 75.93 | 84.02 | 73.76 | 79.25 | 76.78 | 82.98 | 74.17 | 81.89 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.422 | 0.52 | 0.91 | 1.198 | 0.554 | 0.422 | 0.74 | 0.412 | 0.488 | 1.504 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3966 | 3148 | -20.6% | -1344 to -293.1 | GAIN |
| response time (ms), 99th percentile | 5915 | 5202 | -12.1% | -1232 to -194.3 | GAIN |
| time over the response line (% of samples) | 48.48 | 49.47 | +2.0% | -0.5145 to +2.482 | STEADY, inside the noise (up) |
| failed requests (%) | 32.23 | 36.26 | +12.5% | +2.288 to +5.774 | LOSS |
| HPA replicas, mean | 9.787 | 12.29 | +25.6% | +1.932 to +3.076 | power given |
| pods started | 4.42 | 9.98 | +125.8% | +4.674 to +6.446 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.513e-16 to +2.671e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.2 | 276 | -0.1% | -0.6477 to +0.2492 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.2 | 276 | -0.1% | -0.6477 to +0.2492 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.408 | 2.453 | +1.8% | +0.03286 to +0.05586 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.97 | 75.49 | +6.4% | +4.187 to +4.855 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.422 | 0.52 | +23.2% | +0.05297 to +0.143 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4534 | 3768 | -16.9% | -1406 to -124.9 | GAIN |
| response time (ms), 99th percentile | 6707 | 6194 | -7.6% | -1039 to +15.02 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 58.05 | 59.93 | +3.2% | -0.00256 to +3.763 | STEADY, inside the noise (up) |
| failed requests (%) | 41.86 | 44.42 | +6.1% | +0.2036 to +4.916 | LOSS |
| HPA replicas, mean | 9.818 | 11.32 | +15.3% | +0.8848 to +2.126 | power given |
| pods started | 3.9 | 6.5 | +66.7% | +1.624 to +3.576 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +6.142e-16 to +1.695e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.7 | 277.7 | -0.0% | -0.697 to +0.5433 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.7 | 277.7 | -0.0% | -0.697 to +0.5433 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.507 | 2.551 | +1.8% | +0.02708 to +0.06134 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.93 | 84.02 | +10.7% | +7.699 to +8.477 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.91 | 1.198 | +31.6% | +0.2168 to +0.3592 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3872 | 2659 | -31.3% | -1694 to -732.4 | GAIN |
| response time (ms), 99th percentile | 6235 | 5284 | -15.3% | -1441 to -461.3 | GAIN |
| time over the response line (% of samples) | 54.73 | 53.15 | -2.9% | -2.632 to -0.5469 | GAIN |
| failed requests (%) | 39.05 | 43.21 | +10.6% | +1.711 to +6.606 | LOSS |
| HPA replicas, mean | 9.8 | 11.51 | +17.4% | +1.149 to +2.262 | power given |
| pods started | 4.2 | 9.14 | +117.6% | +3.771 to +6.109 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +7.934e-17 to +8.444e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.3 | 276.2 | -0.1% | -0.606 to +0.3002 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.3 | 276.2 | -0.1% | -0.606 to +0.3002 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.416 | 2.457 | +1.7% | +0.02701 to +0.05415 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.76 | 79.25 | +7.4% | +5.078 to +5.89 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.554 | 0.422 | -23.8% | -0.1781 to -0.0859 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 5 (response time (ms), 95th percentile; time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 1

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4334 | 3418 | -21.1% | -1575 to -257 | GAIN |
| response time (ms), 99th percentile | 6531 | 6188 | -5.3% | -901.1 to +214.5 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 61.04 | 59.48 | -2.6% | -2.675 to -0.4548 | GAIN |
| failed requests (%) | 43.58 | 47.78 | +9.6% | +1.655 to +6.736 | LOSS |
| HPA replicas, mean | 9.83 | 11.05 | +12.4% | +0.6738 to +1.758 | power given |
| pods started | 3.82 | 7.28 | +90.6% | +2.342 to +4.578 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +6.439e-16 to +1.665e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.8 | 277 | -0.3% | -1.106 to -0.3359 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.8 | 277 | -0.3% | -1.106 to -0.3359 | GAIN |
| CPU used with Omni's own (cores), mean | 2.499 | 2.536 | +1.5% | +0.02339 to +0.04985 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.78 | 82.98 | +8.1% | +5.901 to +6.497 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.74 | 0.412 | -44.3% | -0.3686 to -0.2874 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 5

49 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3794 | 3358 | -11.5% | -1236 to +362.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5870 | 5675 | -3.3% | -920 to +530 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 52.84 | 53.02 | +0.3% | -1.621 to +1.976 | STEADY, inside the noise (up) |
| failed requests (%) | 39.59 | 40.94 | +3.4% | -1.463 to +4.164 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.802 | 11.91 | +21.5% | +1.463 to +2.761 | power given |
| pods started | 4.163 | 7.878 | +89.2% | +2.767 to +4.662 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003669 to +0.001232 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.6 | 277.2 | +0.2% | +0.1093 to +1.185 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.6 | 277.2 | +0.2% | +0.1152 to +1.102 | power given |
| CPU used with Omni's own (cores), mean | 2.451 | 2.502 | +2.1% | +0.03191 to +0.07143 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.05 | 81.89 | +10.6% | +7.402 to +8.284 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.4878 | 1.504 | +208.4% | +0.1605 to +1.872 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
