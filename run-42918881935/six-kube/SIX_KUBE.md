# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2632 | 3583 | 2585 | 3634 |
| response time (ms), 99th percentile | 5566 | 6146 | 4708 | 5584 |
| time over the response line (% of samples) | 44.08 | 40.82 | 35.99 | 36.89 |
| failed requests (%) | 24.62 | 24.96 | 15.84 | 19.24 |
| HPA replicas, mean | 9.672 | 13.05 | 9.661 | 13.07 |
| pods started | 4.712 | 10.78 | 4.816 | 9.904 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.8 | 183.7 | 183.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.8 | 183.7 | 183.7 |
| CPU used with Omni's own (cores), mean | 2.407 | 2.451 | 2.322 | 2.379 |
| host CPU busy, the real machine under kind (%) | 70.62 | 72.72 | 69.57 | 73.77 |
| organism work | 2.226e+11 | 2.226e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 5.689e+11 | 5.69e+11 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.574 | 2.478 | 2.61 | 2.524 |
| organism work per energy | 0.3913 | 0.3912 | 0.012 | 0.012 |
| organism behind its window (s) | 0.0048 | 0.0088 | 0.1504 | 0.1632 |

## Each organism: omni against native, paired by repetition

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

125 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2632 | 3583 | +36.1% | +574 to +1328 | LOSS |
| response time (ms), 99th percentile | 5566 | 6146 | +10.4% | +275.2 to +884.2 | LOSS |
| time over the response line (% of samples) | 44.08 | 40.82 | -7.4% | -4.099 to -2.431 | GAIN |
| failed requests (%) | 24.62 | 24.96 | +1.4% | -0.2431 to +0.9238 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.672 | 13.05 | +34.9% | +3.042 to +3.717 | power given |
| pods started | 4.712 | 10.78 | +128.7% | +5.665 to +6.463 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.24e-16 to +1.109e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.8 | +0.3% | +0.3183 to +0.8142 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.8 | +0.3% | +0.3183 to +0.8142 | power given |
| CPU used with Omni's own (cores), mean | 2.407 | 2.451 | +1.8% | +0.03918 to +0.04847 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.62 | 72.72 | +3.0% | +1.961 to +2.241 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.0048 | 0.0088 | +83.3% | -0.002115 to +0.01012 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

125 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2585 | 3634 | +40.6% | +769.2 to +1328 | LOSS |
| response time (ms), 99th percentile | 4708 | 5584 | +18.6% | +528.4 to +1223 | LOSS |
| time over the response line (% of samples) | 35.99 | 36.89 | +2.5% | -0.09538 to +1.896 | STEADY, inside the noise (up) |
| failed requests (%) | 15.84 | 19.24 | +21.5% | +2.464 to +4.338 | LOSS |
| HPA replicas, mean | 9.661 | 13.07 | +35.3% | +3.02 to +3.804 | power given |
| pods started | 4.816 | 9.904 | +105.6% | +4.67 to +5.506 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0009336 to +0.0003068 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 183.7 | +0.0% | -0.1922 to +0.2145 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 183.7 | +0.0% | -0.2012 to +0.2109 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.322 | 2.379 | +2.5% | +0.05204 to +0.06261 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.57 | 73.77 | +6.0% | +4.039 to +4.342 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1504 | 0.1632 | +8.5% | +0.0006992 to +0.0249 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The spine, the muscles every stack runs on
- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- The whole tower, every muscle once

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
