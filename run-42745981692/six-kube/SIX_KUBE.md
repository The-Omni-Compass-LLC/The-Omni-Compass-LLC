# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on: native | The spine, the muscles every stack runs on: omni | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1389 | 1423 | 1215 | 1261 | 1634 | 1427 | 1603 | 1588 | 1280 | 1474 |
| response time (ms), 99th percentile | 4528 | 4728 | 4485 | 4862 | 4970 | 4739 | 4769 | 4719 | 4296 | 4530 |
| time over the response line (% of samples) | 15.61 | 11.88 | 20.35 | 15.01 | 17.15 | 13.36 | 22.31 | 17.63 | 22.53 | 18.19 |
| failed requests (%) | 4.943 | 4.39 | 7.971 | 6.806 | 5.578 | 5.553 | 8.441 | 7.022 | 9.845 | 9.008 |
| HPA replicas, mean | 9.556 | 14.19 | 9.648 | 14.36 | 9.574 | 14.07 | 9.592 | 14.36 | 9.638 | 14.19 |
| pods started | 5.64 | 11.6 | 5.1 | 12.16 | 5.32 | 11 | 5.16 | 11.76 | 5 | 12.26 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 178.8 | 179.2 | 181.2 | 180.3 | 179.2 | 179.6 | 181.3 | 180.5 | 181.1 | 180.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.8 | 179.2 | 181.2 | 180.3 | 179.2 | 179.6 | 181.3 | 180.5 | 181.1 | 180.6 |
| CPU used with Omni's own (cores), mean | 1.86 | 1.91 | 2.036 | 2.067 | 1.903 | 1.954 | 2.04 | 2.067 | 2.028 | 2.075 |
| host CPU busy, the real machine under kind (%) | 55.46 | 56.99 | 60.72 | 61.94 | 56.83 | 58.47 | 60.6 | 61.86 | 60.58 | 62.49 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.03 | 0.092 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1389 | 1423 | +2.4% | -184.6 to +252.3 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4528 | 4728 | +4.4% | -95.62 to +495 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 15.61 | 11.88 | -23.9% | -4.65 to -2.802 | GAIN |
| failed requests (%) | 4.943 | 4.39 | -11.2% | -0.953 to -0.1542 | GAIN |
| HPA replicas, mean | 9.556 | 14.19 | +48.5% | +4.3 to +4.962 | power given |
| pods started | 5.64 | 11.6 | +105.7% | +5.466 to +6.454 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.794e-16 to +8.203e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.8 | 179.2 | +0.2% | +0.06805 to +0.7174 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.8 | 179.2 | +0.2% | +0.06805 to +0.7174 | power given |
| CPU used with Omni's own (cores), mean | 1.86 | 1.91 | +2.7% | +0.03869 to +0.06015 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.46 | 56.99 | +2.8% | +1.279 to +1.772 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.985e+05 to +8.004e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.424e-05 to -9.402e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 1

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1215 | 1261 | +3.8% | -76.91 to +168.6 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4485 | 4862 | +8.4% | +16.66 to +737.7 | LOSS |
| time over the response line (% of samples) | 20.35 | 15.01 | -26.2% | -6.769 to -3.902 | GAIN |
| failed requests (%) | 7.971 | 6.806 | -14.6% | -1.747 to -0.5825 | GAIN |
| HPA replicas, mean | 9.648 | 14.36 | +48.8% | +4.476 to +4.946 | power given |
| pods started | 5.1 | 12.16 | +138.4% | +6.629 to +7.491 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.931e-16 to +1.734e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.2 | 180.3 | -0.5% | -1.367 to -0.4522 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.2 | 180.3 | -0.5% | -1.367 to -0.4522 | GAIN |
| CPU used with Omni's own (cores), mean | 2.036 | 2.067 | +1.5% | +0.01935 to +0.04297 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.72 | 61.94 | +2.0% | +0.9088 to +1.529 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.621e+05 to +8.625e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.149e-05 to -8.145e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1634 | 1427 | -12.6% | -475.3 to +62.59 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4970 | 4739 | -4.6% | -495.2 to +34.16 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 17.15 | 13.36 | -22.1% | -4.704 to -2.885 | GAIN |
| failed requests (%) | 5.578 | 5.553 | -0.5% | -0.3239 to +0.2733 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.574 | 14.07 | +47.0% | +4.069 to +4.922 | power given |
| pods started | 5.32 | 11 | +106.8% | +5.181 to +6.179 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.655e-16 to +4.431e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.2 | 179.6 | +0.2% | -0.02676 to +0.7197 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.2 | 179.6 | +0.2% | -0.02676 to +0.7197 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.903 | 1.954 | +2.7% | +0.04314 to +0.05971 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.83 | 58.47 | +2.9% | +1.392 to +1.895 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1603 | 1588 | -1.0% | -158.6 to +127.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4769 | 4719 | -1.0% | -440.4 to +340.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 22.31 | 17.63 | -21.0% | -6.199 to -3.152 | GAIN |
| failed requests (%) | 8.441 | 7.022 | -16.8% | -2.283 to -0.5556 | GAIN |
| HPA replicas, mean | 9.592 | 14.36 | +49.7% | +4.522 to +5.007 | power given |
| pods started | 5.16 | 11.76 | +127.9% | +6.148 to +7.052 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.661e-16 to +2.108e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.3 | 180.5 | -0.4% | -1.112 to -0.5164 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.3 | 180.5 | -0.4% | -1.112 to -0.5164 | GAIN |
| CPU used with Omni's own (cores), mean | 2.04 | 2.067 | +1.3% | +0.01579 to +0.03903 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.6 | 61.86 | +2.1% | +0.942 to +1.581 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 1

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1280 | 1474 | +15.2% | +15.57 to +373.4 | LOSS |
| response time (ms), 99th percentile | 4296 | 4530 | +5.5% | -181.8 to +650.3 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 22.53 | 18.19 | -19.3% | -5.827 to -2.859 | GAIN |
| failed requests (%) | 9.845 | 9.008 | -8.5% | -1.578 to -0.09427 | GAIN |
| HPA replicas, mean | 9.638 | 14.19 | +47.2% | +4.248 to +4.849 | power given |
| pods started | 5 | 12.26 | +145.2% | +6.683 to +7.837 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.779e-16 to +4.621e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 180.6 | -0.2% | -0.8599 to -0.03545 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 180.6 | -0.2% | -0.8599 to -0.03545 | GAIN |
| CPU used with Omni's own (cores), mean | 2.028 | 2.075 | +2.3% | +0.03108 to +0.06318 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.58 | 62.49 | +3.2% | +1.491 to +2.327 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0.03 | 0.092 | +206.7% | +0.001253 to +0.1227 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Energy / Facility / Industrial
- Distribution / Specialized

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
