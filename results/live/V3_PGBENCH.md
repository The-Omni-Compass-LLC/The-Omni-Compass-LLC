# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number (a resource spent that rose reads **power given**, never a loss; the key: `docs/HOW_TO_READ_THE_RESULTS.md`)); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any increase in any run is marked. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38054754511 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 3 |
| B | 38054758150 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 3 |
| C | 38054761503 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 39,229, 16,729, 26,435 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 17,233 | 17,193 | -0.2% (-1.5 to +1.0) | -0.1% (-0.4 to +0.2) | -0.0% (-0.1 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 17,255 | 17,256 | +0.0% (-0.1 to +0.1) | -0.1% (-0.2 to +0.1) | -0.0% (-0.1 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms, lag included) | 7.14 | 8.95 | +25.5% (-255.2 to +306.1) | -17.9% (-60.1 to +24.3) | -0.5% (-35.0 to +33.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 19.3 | 29.3 | +51.5% (-202.2 to +305.2) | -2.8% (-45.8 to +40.1) | +4.3% (-39.6 to +48.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, median (ms) | 0.22 | 0.222 | +0.9% (-5.9 to +7.7) | -0.9% (-4.6 to +2.9) | +0.1% (-2.6 to +2.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.23 | 1.64 | +32.9% (-174.3 to +240.2) | +0.5% (-38.8 to +39.8) | +2.3% (-25.6 to +30.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 19.6 | 17.7 | -9.6% (-20.3 to +1.1) | -6.7% (-11.4 to -1.9) | -7.2% (-8.1 to -6.4) | STEADY, no difference beyond the noise (1 of 3 runs) |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | +0.0% (+0.0 to +0.0) | +1.7% (-5.5 to +8.8) | STEADY, no difference beyond the noise (2 of 3 runs) |
| host CPU busy (share of the run) | 0.468 | 0.471 | +0.7% (-2.5 to +3.8) | -0.7% (-3.1 to +1.7) | -0.1% (-1.7 to +1.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 807.4 | 814.2 | +0.8% (-2.4 to +4.0) | -0.8% (-3.8 to +2.1) | -0.1% (-1.8 to +1.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.104 | 0.105 | +1.1% (-2.4 to +4.5) | -0.7% (-3.9 to +2.4) | -0.0% (-1.8 to +1.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 4.44 | 5.08 | +14.4% (+7.8 to +21.0) | +31.7% (+25.3 to +38.1) | +16.4% (+15.3 to +17.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.0 | -10.2% (-25.7 to +5.3) | -6.0% (-10.7 to -1.3) | -6.4% (-12.1 to -0.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 14 to 21 (12 trials, 7 allowed, 3 refused); acting: 8 to 21 (16 trials, 13 allowed, 2 refused); acting: 14 to 21 (13 trials, 7 allowed, 3 refused); run B: acting: 17 to 20 (9 trials, 3 allowed, 5 refused); acting: 15 to 20 (10 trials, 5 allowed, 4 refused); acting: 17 to 20 (8 trials, 3 allowed, 5 refused); run C: acting: 17 to 20 (10 trials, 3 allowed, 6 refused); acting: 13 to 20 (12 trials, 7 allowed, 4 refused); acting: 17 to 20 (9 trials, 3 allowed, 5 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,754, 4,448, 7,385 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,611 | 1,613 | +0.1% (-1.1 to +1.3) | +24.9% (-47.5 to +97.4) | -0.5% (-3.3 to +2.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 1,653 | 1,652 | -0.1% (-0.2 to +0.1) | +1.7% (-7.7 to +11.2) | -0.2% (-0.3 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms, lag included) | 6.46 | 6.18 | -4.3% (-28.3 to +19.8) | -60.9% (-300.3 to +178.4) | +21.8% (-24.1 to +67.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 198.8 | 182.9 | -8.0% (-37.9 to +21.8) | -61.6% (-301.5 to +178.4) | -4.4% (-23.9 to +15.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, median (ms) | 1.53 | 1.53 | -0.1% (-0.9 to +0.8) | -81.5% (-263.9 to +100.9) | -0.4% (-2.6 to +1.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 6.5 | 6.1 | -6.1% (-39.2 to +27.0) | -64.2% (-296.7 to +168.3) | +6.5% (-25.1 to +38.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.2 | -4.0% (-5.1 to -2.8) | +2.2% (+0.8 to +3.6) | -3.5% (-6.5 to -0.6) | **the runs disagree** |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | +11.7% (+4.5 to +18.8) | +11.7% (+4.5 to +18.8) | **power given in all three of our runs** |
| host CPU busy (share of the run) | 0.336 | 0.336 | +0.0% (-1.0 to +1.0) | +2.1% (-8.6 to +12.8) | +0.1% (-2.2 to +2.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 506.2 | 506.2 | +0.0% (-1.2 to +1.2) | +1.5% (-7.5 to +10.4) | +0.1% (-2.1 to +2.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.698 | 0.698 | -0.1% (-2.2 to +2.0) | -17.8% (-63.1 to +27.5) | +0.6% (-2.1 to +3.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1 | 1.81 | +80.9% (+77.8 to +84.1) | +76.0% (+70.8 to +81.2) | +48.9% (+43.8 to +54.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.4 | -2.9% (-4.7 to -1.1) | +1.9% (+1.0 to +2.8) | -2.9% (-6.1 to +0.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 19 to 22 (16 trials, 3 allowed, 6 refused); acting: 19 to 21 (14 trials, 2 allowed, 7 refused); acting: 19 to 20 (11 trials, 1 allowed, 7 refused); run B: acting: 20 to 21 (24 trials, 1 allowed, 2 refused); acting: 20 to 22 (26 trials, 2 allowed, 1 refused); acting: 20 to 22 (25 trials, 2 allowed, 1 refused); run C: acting: 18 to 22 (17 trials, 4 allowed, 7 refused); acting: 16 to 22 (22 trials, 6 allowed, 5 refused); acting: 18 to 22 (16 trials, 4 allowed, 7 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 1,922, 1,867, 3,130 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 845.0 | 845.9 | +0.1% (-0.5 to +0.7) | +0.0% (-0.2 to +0.3) | +0.3% (-1.3 to +1.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 845.0 | 846.0 | +0.1% (-0.4 to +0.7) | +0.0% (-0.3 to +0.4) | +0.1% (-0.1 to +0.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms, lag included) | 4.95 | 5.24 | +6.0% (-8.3 to +20.3) | -2.7% (-33.0 to +27.6) | -1.6% (-44.7 to +41.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 9.71 | 12.4 | +27.6% (-28.4 to +83.5) | +2.1% (-57.7 to +61.8) | -52.4% (-379.5 to +274.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, median (ms) | 1.87 | 1.87 | -0.1% (-0.7 to +0.6) | -1.4% (-6.7 to +3.8) | -0.3% (-2.1 to +1.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 2.39 | 2.49 | +4.2% (-5.4 to +13.9) | -0.4% (-20.1 to +19.2) | -9.6% (-102.2 to +83.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 19.5 | 16.9 | -13.4% (-26.9 to -0.0) | -7.0% (-12.4 to -1.5) | -11.0% (-22.0 to -0.0) | **GAIN in all three of our runs** |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +1.7% (-5.5 to +8.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU busy (share of the run) | 0.231 | 0.231 | +0.2% (-1.0 to +1.3) | -1.9% (-8.1 to +4.4) | +0.0% (-2.6 to +2.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 359.4 | 360.1 | +0.2% (-1.0 to +1.4) | -1.9% (-8.3 to +4.5) | +0.1% (-2.5 to +2.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.945 | 0.946 | +0.1% (-1.2 to +1.4) | -1.9% (-8.2 to +4.3) | -0.2% (-4.3 to +3.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.763 | 1.49 | +95.9% (+90.3 to +101.5) | +96.4% (+89.1 to +103.7) | +77.2% (+73.0 to +81.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.3 | -13.5% (-31.5 to +4.5) | -5.2% (-5.6 to -4.8) | -8.5% (-19.7 to +2.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 19 to 20 (7 trials, 1 allowed, 6 refused); acting: 9 to 20 (14 trials, 11 allowed, 3 refused); acting: 10 to 20 (14 trials, 10 allowed, 3 refused); run B: acting: 19 to 20 (7 trials, 1 allowed, 6 refused); acting: 19 to 20 (7 trials, 1 allowed, 6 refused); acting: 19 to 20 (7 trials, 1 allowed, 6 refused); run C: acting: 14 to 20 (11 trials, 6 allowed, 4 refused); acting: 18 to 20 (11 trials, 2 allowed, 7 refused); acting: 17 to 20 (9 trials, 3 allowed, 5 refused).

**Across 3 workloads: 1 gauge-rows GAIN, 0 LOSS, 1 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 33 STEADY, 1 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
