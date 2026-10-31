# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38935449417 | `1ccba53a74fe` | omni-v7 (digest d6d467b824c585f1, 46 files) | 4 |
| B | 38947629506 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 4 |
| C | 38957543812 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 976, 976, 975 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365.5 | 364.9 | -0.2% (-0.9 to +0.6) | +0.0% (-0.8 to +0.9) | -0.2% (-0.8 to +0.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 429.2 | 429.1 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,388 | 2,480 | +3.9% (-5.0 to +12.8) | -1.6% (-6.7 to +3.4) | +1.5% (+0.9 to +2.1) | STEADY, no difference beyond the noise (2 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,848 | 3,707 | -3.7% (-13.0 to +5.7) | -3.2% (-23.9 to +17.6) | -0.4% (-3.0 to +2.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 8.6 | 8.54 | -0.8% (-1.6 to +0.1) | -0.2% (-1.0 to +0.7) | -1.0% (-2.6 to +0.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 324.3 | 330.5 | +1.9% (-9.5 to +13.3) | -2.2% (-12.9 to +8.6) | +0.7% (-2.8 to +4.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 1,703 | 1,711 | +0.5% (-1.6 to +2.6) | -1.3% (-8.6 to +6.0) | -0.7% (-4.5 to +3.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 143.6 | 145.7 | +1.5% (-10.1 to +13.1) | -2.5% (-12.3 to +7.2) | +0.7% (-3.1 to +4.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | +7.0% (-18.2 to +32.2) | STEADY, no difference beyond the noise (1 of 3 runs) |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +33.3% (-38.4 to +105.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU busy (share of the run) | 0.313 | 0.312 | -0.2% (-4.0 to +3.6) | -0.3% (-1.7 to +1.1) | -0.6% (-2.3 to +1.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 543.4 | 543.1 | -0.1% (-3.5 to +3.4) | -0.1% (-1.0 to +0.9) | -0.6% (-2.4 to +1.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 3.3 | 3.31 | +0.1% (-2.6 to +2.8) | -0.1% (-1.7 to +1.5) | -0.4% (-2.5 to +1.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +166.7% (+23.2 to +310.1) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 974, 976, 975 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340.1 | 340.0 | -0.0% (-1.6 to +1.6) | -0.2% (-0.6 to +0.2) | -0.4% (-2.8 to +2.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 418.6 | 418.6 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to -0.0) | -0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,522 | 2,504 | -0.7% (-10.1 to +8.7) | +0.7% (-1.9 to +3.3) | -2.1% (-18.3 to +14.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,803 | 3,733 | -1.8% (-13.9 to +10.2) | +2.7% (-11.4 to +16.8) | +0.6% (-14.7 to +16.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 8.86 | 8.9 | +0.5% (-0.9 to +1.8) | -2.6% (-9.6 to +4.4) | -29.1% (-98.2 to +40.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 382.9 | 380.0 | -0.8% (-8.3 to +6.7) | +0.4% (-0.0 to +0.8) | +0.3% (-11.9 to +12.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 1,655 | 1,640 | -0.9% (-2.8 to +1.0) | -0.2% (-3.7 to +3.4) | +1.4% (-7.0 to +9.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 164.5 | 163.2 | -0.8% (-8.1 to +6.4) | +0.2% (-1.2 to +1.5) | +1.3% (-8.2 to +10.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.306 | 0.303 | -0.9% (-4.9 to +3.0) | -0.5% (-6.0 to +5.0) | -0.5% (-3.0 to +1.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 218.9 | 216.8 | -1.0% (-4.9 to +3.0) | -0.4% (-5.9 to +5.0) | -0.5% (-2.9 to +1.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 3.56 | 3.53 | -0.9% (-4.5 to +2.6) | -0.3% (-6.0 to +5.4) | -0.1% (-0.9 to +0.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 390, 389, 393 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 146.7 | 146.1 | -0.4% (-1.7 to +0.8) | +5.1% (-19.1 to +29.3) | -0.0% (-0.6 to +0.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 171.6 | 171.6 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,211 | 2,270 | +2.6% (-18.2 to +23.5) | -32.4% (-167.0 to +102.2) | +0.9% (-2.9 to +4.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,486 | 3,627 | +4.0% (-5.6 to +13.7) | -33.0% (-163.5 to +97.5) | -2.3% (-10.5 to +5.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 11.4 | 11.3 | -0.9% (-3.8 to +2.0) | -0.5% (-3.6 to +2.7) | -0.3% (-0.9 to +0.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 294.4 | 307.7 | +4.5% (-16.1 to +25.1) | -30.3% (-160.9 to +100.3) | -0.9% (-8.0 to +6.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 652.7 | 669.3 | +2.6% (-8.2 to +13.3) | -29.8% (-152.1 to +92.6) | -1.0% (-6.5 to +4.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 53.5 | 56.1 | +4.8% (-13.7 to +23.2) | -30.0% (-159.6 to +99.6) | -1.5% (-8.8 to +5.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | +0.7% (-3.9 to +5.4) | +15.1% (-18.6 to +48.8) | -0.3% (-0.3 to -0.3) | STEADY, no difference beyond the noise (2 of 3 runs) |
| consumers running, most at once | 2 | 2.33 | +16.7% (-55.1 to +88.4) | +50.0% (+50.0 to +50.0) | +0.0% (+0.0 to +0.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| host CPU busy (share of the run) | 0.279 | 0.274 | -1.8% (-6.9 to +3.4) | +0.5% (-3.1 to +4.2) | -0.5% (-2.4 to +1.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 500.3 | 491.4 | -1.8% (-6.9 to +3.3) | +0.6% (-3.1 to +4.4) | -0.5% (-2.3 to +1.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 7.57 | 7.47 | -1.3% (-7.7 to +5.0) | -3.8% (-27.4 to +19.9) | -0.5% (-1.9 to +0.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% (-10.1 to +276.8) | +200.0% (+200.0 to +200.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (3 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: acting: 2 to 3 (2 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,939, 1,938, 1,926 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727.7 | 726.6 | -0.1% (-0.2 to -0.1) | +0.4% (-1.2 to +2.0) | +0.2% (-0.5 to +0.9) | STEADY, no difference beyond the noise (2 of 3 runs) |
| throughput (messages a second consumed) | 852.7 | 852.7 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,418 | 2,434 | +0.6% (-3.7 to +4.9) | -12.6% (-56.9 to +31.8) | -2.2% (-11.3 to +6.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,686 | 3,687 | +0.0% (-6.3 to +6.4) | -10.2% (-51.7 to +31.3) | -2.1% (-11.9 to +7.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 7.7 | 7.61 | -1.2% (-4.2 to +1.7) | -1.3% (-3.4 to +0.7) | -1.5% (-11.3 to +8.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 319.2 | 322.6 | +1.1% (+0.2 to +1.9) | -11.8% (-51.8 to +28.2) | -3.0% (-14.3 to +8.3) | STEADY, no difference beyond the noise (2 of 3 runs) |
| consumer lag, most messages waiting at once | 3,334 | 3,324 | -0.3% (-4.2 to +3.6) | -9.7% (-43.5 to +24.1) | -0.6% (-9.4 to +8.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 278.8 | 279.8 | +0.4% (-0.3 to +1.0) | -11.7% (-51.1 to +27.6) | -2.9% (-14.1 to +8.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +5.9% (-21.0 to +32.9) | +6.3% (-22.3 to +34.9) | +12.4% (-15.0 to +39.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumers running, most at once | 2 | 2.33 | +16.7% (-55.1 to +88.4) | +16.7% (-55.1 to +88.4) | +33.3% (-38.4 to +105.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU busy (share of the run) | 0.338 | 0.34 | +0.5% (-3.1 to +4.1) | -0.1% (-3.8 to +3.5) | -3.3% (-10.8 to +4.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 600.8 | 603.8 | +0.5% (-2.8 to +3.8) | +0.0% (-3.4 to +3.4) | -3.5% (-11.2 to +4.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 1.83 | 1.85 | +0.7% (-2.6 to +3.9) | -0.4% (-2.7 to +2.0) | -3.6% (-11.7 to +4.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% (-10.1 to +276.8) | +166.7% (-120.2 to +453.5) | +166.7% (+23.2 to +310.1) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused).

**Across 3 untouched workloads: 1 gauge-rows GAIN in all three of our runs, 0 LOSS, 0 power given, 41 STEADY, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
