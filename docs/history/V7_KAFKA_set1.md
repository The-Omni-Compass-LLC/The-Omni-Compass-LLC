# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38933446756 | `1ccba53a74fe` | omni-v7 (digest d6d467b824c585f1, 46 files) | 4 |
| B | 38945593946 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 4 |
| C | 38955602669 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 974, 983, 985 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366.4 | 366.1 | -0.1% (-0.7 to +0.6) | -0.2% (-0.7 to +0.4) | -0.1% (-0.8 to +0.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 428.4 | 428.4 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,306 | 2,189 | -5.1% (-12.7 to +2.5) | +2.4% (-8.4 to +13.1) | +2.4% (-2.8 to +7.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,536 | 3,559 | +0.7% (-14.7 to +16.1) | +0.1% (-18.0 to +18.3) | -1.0% (-12.4 to +10.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 8.16 | 8.14 | -0.3% (-2.5 to +1.9) | +0.3% (-0.6 to +1.2) | -0.5% (-1.8 to +0.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 299.4 | 292.7 | -2.2% (-11.2 to +6.7) | +2.3% (-6.6 to +11.1) | +0.7% (-7.5 to +8.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 1,640 | 1,607 | -2.0% (-6.3 to +2.3) | +0.6% (-10.9 to +12.1) | +0.6% (-4.8 to +5.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 132.0 | 129.3 | -2.0% (-9.8 to +5.8) | +2.0% (-7.2 to +11.2) | +0.3% (-6.2 to +6.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.293 | 0.293 | -0.3% (-3.4 to +2.7) | -0.7% (-2.1 to +0.8) | +0.8% (-3.0 to +4.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 523.5 | 522.1 | -0.3% (-3.6 to +3.1) | -0.8% (-2.3 to +0.7) | +0.9% (-2.7 to +4.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 3.17 | 3.17 | -0.2% (-4.1 to +3.7) | -0.7% (-2.3 to +0.9) | +1.0% (-2.0 to +4.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 974, 976, 980 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340.5 | 339.3 | -0.4% (-1.4 to +0.7) | +0.2% (-0.4 to +0.8) | -0.3% (-0.8 to +0.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 418.4 | 418.4 | -0.0% (-0.0 to +0.0) | -0.1% (-0.5 to +0.3) | -0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,466 | 2,532 | +2.6% (-3.5 to +8.8) | -0.5% (-6.1 to +5.0) | +0.7% (-10.2 to +11.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,752 | 3,716 | -1.0% (-9.2 to +7.2) | -2.9% (-19.5 to +13.8) | -2.0% (-19.2 to +15.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 9.39 | 9.37 | -0.3% (-2.6 to +2.1) | -1.0% (-5.0 to +3.0) | +0.8% (-0.7 to +2.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 378.2 | 387.2 | +2.4% (-6.6 to +11.3) | -2.8% (-8.8 to +3.2) | +0.5% (+0.0 to +1.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| consumer lag, most messages waiting at once | 1,647 | 1,640 | -0.4% (-5.6 to +4.8) | -2.1% (-7.7 to +3.5) | -1.9% (-2.7 to -1.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| consumer lag, mean messages waiting | 164.0 | 166.7 | +1.6% (-6.0 to +9.3) | -3.3% (-10.3 to +3.7) | +0.7% (-1.3 to +2.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.293 | 0.291 | -0.8% (-6.1 to +4.5) | -1.2% (-6.0 to +3.5) | -0.3% (-4.0 to +3.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 205.3 | 203.8 | -0.8% (-6.1 to +4.6) | -1.2% (-6.0 to +3.7) | -0.3% (-4.1 to +3.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 3.34 | 3.32 | -0.4% (-4.7 to +3.9) | -1.5% (-5.5 to +2.6) | +0.0% (-4.0 to +4.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 391, 392, 393 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 146.5 | 146.1 | -0.2% (-0.9 to +0.4) | -0.1% (-0.2 to +0.0) | +0.4% (-0.0 to +0.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 171.7 | 171.7 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,249 | 2,351 | +4.5% (-6.1 to +15.2) | +1.7% (-4.0 to +7.3) | -9.1% (-34.5 to +16.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,633 | 3,619 | -0.4% (-16.9 to +16.2) | -2.5% (-13.5 to +8.6) | -7.0% (-24.5 to +10.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 11.4 | 11.5 | +0.8% (-2.6 to +4.3) | -0.3% (-1.0 to +0.3) | -0.4% (-1.6 to +0.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 306.4 | 313.9 | +2.4% (-7.8 to +12.7) | -0.2% (-4.9 to +4.4) | -9.6% (-24.3 to +5.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 674.0 | 669.7 | -0.6% (-14.0 to +12.7) | +3.0% (-0.6 to +6.5) | -6.6% (-26.5 to +13.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 56.4 | 56.7 | +0.4% (-8.0 to +8.9) | -0.4% (-7.1 to +6.2) | -9.4% (-22.1 to +3.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.277 | 0.281 | +1.6% (-6.2 to +9.3) | -0.9% (-2.1 to +0.3) | -1.2% (-2.3 to -0.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 496.3 | 504.2 | +1.6% (-6.1 to +9.3) | -0.9% (-2.1 to +0.3) | -1.1% (-2.3 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 7.52 | 7.66 | +1.8% (-6.4 to +10.0) | -0.8% (-2.1 to +0.5) | -1.5% (-2.7 to -0.4) | STEADY, no difference beyond the noise (2 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,927, 1,929, 1,941 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725.0 | 723.3 | -0.2% (-0.6 to +0.2) | -0.8% (-2.7 to +1.0) | +0.0% (-0.3 to +0.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 847.6 | 847.5 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,237 | 2,275 | +1.7% (-4.3 to +7.7) | +2.5% (-4.0 to +9.1) | -2.7% (-5.4 to -0.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,526 | 3,536 | +0.3% (-5.7 to +6.3) | +2.6% (-0.2 to +5.5) | -0.5% (-3.3 to +2.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 8.49 | 8.16 | -3.8% (-16.7 to +9.0) | -2.0% (-12.9 to +8.8) | -2.2% (-15.2 to +10.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 301.3 | 306.3 | +1.7% (-4.2 to +7.5) | +4.1% (+0.1 to +8.0) | -1.9% (-5.9 to +2.2) | STEADY, no difference beyond the noise (2 of 3 runs) |
| consumer lag, most messages waiting at once | 3,171 | 3,181 | +0.3% (-1.7 to +2.3) | +1.2% (-3.5 to +5.9) | -1.8% (-5.1 to +1.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 262.4 | 265.5 | +1.2% (-5.2 to +7.6) | +4.0% (-0.9 to +8.8) | -1.9% (-5.7 to +2.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.4% (-15.0 to +39.8) | +6.2% (-21.1 to +33.4) | -0.3% (-0.3 to -0.3) | STEADY, no difference beyond the noise (2 of 3 runs) |
| consumers running, most at once | 2 | 2.67 | +33.3% (-38.4 to +105.0) | +33.3% (-38.4 to +105.0) | +0.0% (+0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU busy (share of the run) | 0.335 | 0.334 | -0.3% (-1.9 to +1.3) | -0.4% (-1.0 to +0.1) | -0.3% (-3.9 to +3.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 575.4 | 574.2 | -0.2% (-2.0 to +1.6) | -0.4% (-1.0 to +0.2) | -0.3% (-4.8 to +4.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 1.76 | 1.76 | +0.0% (-2.1 to +2.1) | +0.5% (-0.8 to +1.8) | -0.3% (-5.1 to +4.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% (+23.2 to +310.1) | +200.0% (-48.4 to +448.4) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 2 gauge-rows GAIN in all three of our runs, 0 LOSS, 0 power given, 40 STEADY, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
