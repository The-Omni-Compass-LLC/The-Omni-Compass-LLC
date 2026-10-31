# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38935420705 | `1ccba53a74fe` | omni-v7 (digest d6d467b824c585f1, 46 files) | 3 |
| B | 38945602041 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 3 |
| C | 38957516288 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 16,457, 16,228, 26,361 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7,242 | 7,242 | -0.0% (-0.2 to +0.2) | +0.0% (-0.2 to +0.2) | -0.1% (-0.3 to +0.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 7,242 | 7,242 | -0.0% (-0.2 to +0.2) | +0.0% (-0.2 to +0.2) | -0.0% (-0.2 to +0.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms, lag included) | 1.32 | 1.25 | -5.2% (-42.1 to +31.7) | +10.2% (-7.6 to +28.1) | -9.6% (-20.2 to +1.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 3.93 | 3.66 | -6.9% (-64.8 to +51.0) | +21.6% (-14.2 to +57.4) | -16.1% (-19.4 to -12.8) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, median (ms) | 0.367 | 0.366 | -0.1% (-1.8 to +1.6) | +0.5% (-1.2 to +2.3) | -0.5% (-2.0 to +1.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.561 | 0.538 | -4.2% (-31.4 to +23.1) | +6.2% (-5.2 to +17.6) | -6.5% (-14.4 to +1.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 19.5 | 18.4 | -5.6% (-13.6 to +2.4) | -6.0% (-13.6 to +1.5) | -6.9% (-8.4 to -5.4) | STEADY, no difference beyond the noise (2 of 3 runs) |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.318 | 0.317 | -0.3% (-3.2 to +2.6) | +1.0% (-1.6 to +3.6) | -0.3% (-1.5 to +0.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 467.1 | 465.6 | -0.3% (-3.7 to +3.1) | +1.1% (-1.9 to +4.2) | -0.4% (-1.5 to +0.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.143 | -0.3% (-3.5 to +2.9) | +1.1% (-1.9 to +4.2) | -0.3% (-1.3 to +0.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.58 | 3.33 | +29.1% (+28.3 to +29.9) | +30.5% (+27.2 to +33.9) | +23.1% (+17.3 to +28.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.3% (-5.6 to -5.0) | -5.2% (-5.6 to -4.8) | -5.6% (-7.5 to -3.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); run B: acting: 18 to 20 (7 trials, 2 allowed, 5 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); run C: acting: 17 to 20 (8 trials, 3 allowed, 4 refused); acting: 18 to 20 (7 trials, 2 allowed, 5 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 6,966, 3,773, 6,039 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,875 | 2,880 | +0.2% (-2.9 to +3.3) | +0.3% (-4.4 to +5.0) | +1.0% (-6.3 to +8.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 3,062 | 3,060 | -0.1% (-0.6 to +0.4) | -0.1% (-0.5 to +0.2) | +0.0% (-0.7 to +0.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms, lag included) | 112.6 | 101.5 | -9.9% (-114.5 to +94.8) | +1.9% (-76.9 to +80.8) | -41.4% (-423.7 to +340.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 621.8 | 580.9 | -6.6% (-25.2 to +12.1) | -20.0% (-161.9 to +122.0) | -13.5% (-84.8 to +57.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, median (ms) | 0.712 | 0.733 | +3.0% (-3.9 to +9.8) | +1.1% (-3.4 to +5.7) | +0.3% (-1.8 to +2.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 22.7 | 20.8 | -8.3% (-44.9 to +28.2) | -13.3% (-140.8 to +114.3) | -20.3% (-150.9 to +110.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.8 | -0.9% (-6.8 to +4.9) | -1.8% (-5.8 to +2.2) | -4.4% (-5.3 to -3.5) | STEADY, no difference beyond the noise (2 of 3 runs) |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (-2.4 to +22.4) | +8.3% (+1.2 to +15.5) | +5.0% (+5.0 to +5.0) | STEADY, no difference beyond the noise (1 of 3 runs) |
| host CPU busy (share of the run) | 0.334 | 0.342 | +2.6% (-1.3 to +6.5) | +0.8% (-1.9 to +3.6) | +0.6% (+0.0 to +1.2) | STEADY, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 569.2 | 584.1 | +2.6% (-1.6 to +6.8) | +0.8% (-2.5 to +4.2) | +0.6% (-0.1 to +1.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.44 | 0.451 | +2.4% (-5.0 to +9.8) | +0.5% (-7.3 to +8.4) | -0.4% (-8.3 to +7.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.852 | 1.41 | +65.8% (+62.2 to +69.5) | +79.4% (+72.8 to +86.0) | +55.1% (+46.2 to +63.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.9 | -0.7% (-6.1 to +4.8) | -1.3% (-6.4 to +3.9) | -3.5% (-4.1 to -3.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 19 to 21 (17 trials, 2 allowed, 4 refused); acting: 19 to 22 (17 trials, 3 allowed, 2 refused); acting: 20 to 21 (15 trials, 1 allowed, 5 refused); run B: acting: 20 to 21 (12 trials, 1 allowed, 5 refused); acting: 19 to 20 (9 trials, 1 allowed, 6 refused); acting: 19 to 21 (11 trials, 2 allowed, 4 refused); run C: acting: 17 to 20 (16 trials, 3 allowed, 3 refused); acting: 19 to 21 (18 trials, 2 allowed, 4 refused); acting: 18 to 20 (14 trials, 2 allowed, 6 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 2,118, 1,921, 2,250 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 931.0 | 926.0 | -0.5% (-1.6 to +0.6) | +15.7% (-15.5 to +46.9) | -0.0% (-1.1 to +1.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 931.9 | 930.7 | -0.1% (-0.6 to +0.4) | +0.1% (-0.4 to +0.5) | -0.1% (-0.5 to +0.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms, lag included) | 3.54 | 3.79 | +7.0% (-35.1 to +49.1) | -18.6% (-55.3 to +18.2) | -7.6% (-37.8 to +22.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 8.39 | 19.5 | +132.7% (-392.4 to +657.7) | +18.8% (-73.1 to +110.7) | -26.2% (-129.6 to +77.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, median (ms) | 1.5 | 1.51 | +0.6% (-5.3 to +6.6) | -80.7% (-412.5 to +251.2) | +0.3% (-1.5 to +2.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 2.01 | 3.63 | +80.4% (-173.1 to +333.9) | -26.9% (-114.8 to +61.0) | -2.6% (-47.2 to +42.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 19.4 | 17.2 | -11.1% (-20.3 to -2.0) | -0.5% (-3.0 to +2.1) | -7.3% (-9.9 to -4.7) | STEADY, no difference beyond the noise (1 of 3 runs) |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +5.0% (+5.0 to +5.0) | +0.0% (+0.0 to +0.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| host CPU busy (share of the run) | 0.285 | 0.287 | +0.6% (-5.7 to +6.9) | -2.6% (-6.0 to +0.9) | -0.1% (-1.3 to +1.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 492.3 | 495.2 | +0.6% (-5.8 to +6.9) | -2.8% (-6.7 to +1.1) | -0.1% (-1.4 to +1.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 1.18 | 1.19 | +1.1% (-5.9 to +8.2) | -16.7% (-51.1 to +17.7) | -0.1% (-2.5 to +2.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.817 | 1.61 | +96.6% (+92.8 to +100.4) | +92.3% (+85.1 to +99.4) | +91.7% (+86.7 to +96.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.8 | -11.2% (-22.5 to +0.0) | -0.4% (-2.8 to +2.1) | -5.6% (-7.6 to -3.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 16 to 20 (9 trials, 4 allowed, 3 refused); acting: 15 to 20 (9 trials, 5 allowed, 3 refused); acting: 17 to 20 (9 trials, 3 allowed, 4 refused); run B: left native (26 trials, 0 allowed, 0 refused); acting: 19 to 20 (24 trials, 1 allowed, 2 refused); left native (26 trials, 0 allowed, 1 refused); run C: acting: 18 to 20 (8 trials, 2 allowed, 4 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused).

**Across 3 workloads: 0 gauge-rows GAIN in all three of our runs, 0 LOSS, 0 power given, 36 STEADY, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
