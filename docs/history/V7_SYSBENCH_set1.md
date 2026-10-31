# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38935427838 | `1ccba53a74fe` | omni-v7 (digest d6d467b824c585f1, 46 files) | 5 |
| B | 38945609870 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 5 |
| C | 38957523334 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,935 | 2,934 | -0.1% (-0.2 to +0.1) | +0.0% (-0.1 to +0.2) | +0.2% (-1.3 to +1.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 2,940 | 2,939 | -0.1% (-0.3 to +0.2) | +0.0% (-0.2 to +0.2) | -0.1% (-0.4 to +0.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| queries a second | 2,940 | 2,939 | -0.1% (-0.3 to +0.2) | +0.0% (-0.2 to +0.2) | -0.1% (-0.4 to +0.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.284 | 0.279 | -1.6% (-10.0 to +6.7) | +1.8% (-10.1 to +13.7) | -2.0% (-24.9 to +20.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.456 | 0.445 | -2.3% (-9.0 to +4.3) | -1.2% (-12.3 to +9.9) | -3.4% (-29.9 to +23.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.183 | 0.186 | +1.5% (-2.8 to +5.8) | +2.3% (-7.7 to +12.3) | -0.2% (-15.0 to +14.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 462.3 | -9.7% (-23.7 to +4.3) | -5.7% (-21.9 to +10.4) | -4.0% (-20.6 to +12.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| pages holding data, mean (MB) | 463.5 | 422.9 | -8.8% (-22.0 to +4.5) | -7.7% (-29.5 to +14.1) | -4.2% (-21.5 to +13.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| pages read from disk into the pool (misses) | 367,298 | 413,907 | +12.7% (-13.3 to +38.7) | +12.1% (-38.6 to +62.8) | +4.3% (-23.3 to +31.9) | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.146 | +0.0% (-2.9 to +2.9) | +4.1% (-16.4 to +24.6) | -0.6% (-14.5 to +13.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 263.5 | 263.4 | -0.0% (-2.8 to +2.8) | +4.3% (-16.8 to +25.3) | -0.6% (-14.2 to +13.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.195 | 0.196 | +0.1% (-2.6 to +2.8) | +4.2% (-16.9 to +25.3) | -0.8% (-15.7 to +14.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 | +10.3 (+2.74 to +17.9) | +10.7 (+3.49 to +17.8) | +14 (+6.55 to +21.5) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 256 to 512 (6 trials, 2 allowed, 2 refused); acting: 384 to 512 (7 trials, 1 allowed, 4 refused); acting: 256 to 512 (4 trials, 2 allowed, 1 refused); run B: acting: 384 to 512 (5 trials, 1 allowed, 2 refused); acting: 384 to 512 (6 trials, 1 allowed, 3 refused); acting: 256 to 640 (8 trials, 3 allowed, 2 refused); run C: acting: 256 to 512 (10 trials, 2 allowed, 4 refused); left native (9 trials, 0 allowed, 4 refused); acting: 384 to 512 (9 trials, 1 allowed, 4 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293.2 | 294.2 | +0.4% (-2.0 to +2.7) | +0.6% (-0.5 to +1.7) | +0.3% (-0.4 to +1.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 293.6 | 294.5 | +0.3% (-1.7 to +2.3) | +0.4% (+0.1 to +0.7) | +0.2% (-0.6 to +1.1) | STEADY, no difference beyond the noise (2 of 3 runs) |
| queries a second | 4,697 | 4,713 | +0.3% (-1.7 to +2.3) | +0.4% (+0.1 to +0.7) | +0.2% (-0.6 to +1.1) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 2.43 | 2.53 | +3.7% (-5.4 to +12.9) | -1.8% (-9.5 to +5.9) | -4.7% (-10.1 to +0.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 3.89 | 4.06 | +4.4% (-1.4 to +10.1) | -5.5% (-29.4 to +18.4) | -5.2% (-9.4 to -1.1) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 1.23 | 1.27 | +2.8% (-8.8 to +14.5) | -2.3% (-10.9 to +6.4) | -0.7% (-2.0 to +0.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 329.3 | -35.7% (-65.3 to -6.0) | -1.9% (-10.4 to +6.5) | -16.5% (-30.6 to -2.3) | STEADY, no difference beyond the noise (1 of 3 runs) |
| pages holding data, mean (MB) | 441.6 | 285.1 | -35.4% (-68.0 to -2.9) | -2.0% (-26.1 to +22.2) | -19.1% (-32.3 to -5.8) | STEADY, no difference beyond the noise (1 of 3 runs) |
| pages read from disk into the pool (misses) | 239,667 | 313,631 | +30.9% (-3.0 to +64.7) | +0.1% (-13.3 to +13.6) | +9.5% (-4.1 to +23.2) | shown, not judged |
| host CPU busy (share of the run) | 0.0917 | 0.093 | +1.5% (-1.4 to +4.3) | +1.8% (-0.9 to +4.4) | +0.9% (-2.6 to +4.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 55.1 | 55.8 | +1.4% (-1.4 to +4.3) | +1.9% (-1.0 to +4.9) | +0.9% (-2.8 to +4.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 1.23 | 1.25 | +1.1% (-1.8 to +3.9) | +1.4% (-0.5 to +3.2) | +0.6% (-2.3 to +3.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 | +3.33 (+1.9 to +4.77) | +8 (+3.03 to +13) | +7 (+4.52 to +9.48) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 256 to 512 (3 trials, 2 allowed, 0 refused); acting: 256 to 512 (3 trials, 2 allowed, 0 refused); acting: 256 to 512 (3 trials, 2 allowed, 0 refused); run B: left native (6 trials, 0 allowed, 2 refused); left native (7 trials, 0 allowed, 2 refused); left native (6 trials, 0 allowed, 1 refused); run C: acting: 256 to 512 (4 trials, 2 allowed, 1 refused); acting: 256 to 512 (3 trials, 2 allowed, 1 refused); left native (4 trials, 0 allowed, 1 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 286.8 | 286.2 | -0.2% (-1.8 to +1.4) | +0.3% (-1.9 to +2.4) | -0.1% (-1.3 to +1.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 296.0 | 296.1 | +0.0% (-0.5 to +0.5) | +0.3% (-1.8 to +2.5) | -0.3% (-1.0 to +0.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| queries a second | 4,737 | 4,737 | +0.0% (-0.5 to +0.5) | +0.3% (-1.8 to +2.5) | -0.3% (-1.0 to +0.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 3.48 | 3.59 | +3.3% (-25.4 to +32.0) | -2.9% (-5.5 to -0.4) | +0.0% (+0.0 to +0.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 98.4 | 109.6 | +11.3% (-120.6 to +143.3) | -2.4% (-5.0 to +0.2) | -9.6% (-61.3 to +42.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 4.81 | 5.31 | +10.5% (-76.2 to +97.1) | -2.1% (-6.4 to +2.1) | -33.4% (-186.1 to +119.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 441.7 | -13.7% (-28.3 to +0.9) | -1.3% (-10.7 to +8.0) | -13.6% (-31.6 to +4.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| pages holding data, mean (MB) | 461.4 | 401.3 | -13.0% (-26.4 to +0.3) | -1.2% (-11.9 to +9.5) | -12.8% (-34.4 to +8.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| pages read from disk into the pool (misses) | 654,505 | 855,267 | +30.7% (-25.9 to +87.2) | -1.1% (-12.2 to +9.9) | +19.5% (-22.1 to +61.0) | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.167 | +0.8% (-3.5 to +5.1) | -2.8% (-8.3 to +2.8) | +0.3% (-3.3 to +3.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 296.4 | 298.8 | +0.8% (-3.5 to +5.1) | -2.8% (-8.9 to +3.2) | +0.3% (-3.3 to +3.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 2.27 | 2.29 | +1.0% (-4.1 to +6.2) | -3.1% (-10.3 to +4.1) | +0.3% (-2.3 to +3.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 | +14.7 (+9.5 to +19.8) | +14 (+5.39 to +22.6) | +12.3 (+3.61 to +21.1) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 128 to 512 (6 trials, 3 allowed, 3 refused); acting: 384 to 512 (9 trials, 1 allowed, 3 refused); left native (10 trials, 0 allowed, 3 refused); run B: left native (13 trials, 0 allowed, 3 refused); acting: 384 to 512 (13 trials, 1 allowed, 4 refused); left native (13 trials, 0 allowed, 3 refused); run C: acting: 256 to 512 (6 trials, 2 allowed, 1 refused); acting: 384 to 512 (8 trials, 1 allowed, 3 refused); acting: 256 to 512 (10 trials, 2 allowed, 3 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192.1 | 191.4 | -0.4% (-2.2 to +1.4) | -0.1% (-2.0 to +1.8) | -0.4% (-0.7 to -0.1) | STEADY, no difference beyond the noise (2 of 3 runs) |
| throughput (transactions a second) | 195.1 | 195.1 | +0.0% (-2.1 to +2.1) | -0.1% (-1.9 to +1.7) | -0.4% (-0.6 to -0.1) | STEADY, no difference beyond the noise (2 of 3 runs) |
| queries a second | 3,901 | 3,902 | +0.0% (-2.1 to +2.1) | -0.1% (-1.9 to +1.7) | -0.4% (-0.6 to -0.1) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 7.3 | 8.03 | +10.1% (+7.2 to +12.9) | +5.5% (-6.6 to +17.7) | -0.6% (-3.2 to +2.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 12.6 | 14.6 | +15.3% (-63.9 to +94.5) | +0.0% (-4.5 to +4.5) | +1.8% (-2.7 to +6.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 4.08 | 4.37 | +7.3% (-7.5 to +22.1) | +0.9% (-7.2 to +9.0) | -0.6% (-3.7 to +2.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 405.0 | -20.9% (-23.9 to -17.9) | -15.5% (-23.1 to -7.8) | +5.6% (-1.3 to +12.4) | STEADY, no difference beyond the noise (1 of 3 runs) |
| pages holding data, mean (MB) | 460.7 | 367.0 | -20.3% (-23.3 to -17.3) | -15.4% (-18.8 to -12.0) | +4.6% (+2.4 to +6.8) | **the runs disagree** |
| pages read from disk into the pool (misses) | 616,349 | 922,398 | +49.7% (+30.6 to +68.7) | +36.3% (+26.0 to +46.6) | -7.6% (-12.3 to -3.0) | shown, not judged |
| host CPU busy (share of the run) | 0.17 | 0.174 | +2.0% (-1.7 to +5.7) | -0.5% (-2.7 to +1.6) | -1.7% (-4.8 to +1.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 308.6 | 314.6 | +1.9% (-1.6 to +5.5) | -0.4% (-2.6 to +1.7) | -1.6% (-4.8 to +1.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 3.49 | 3.57 | +2.4% (-1.7 to +6.5) | -0.4% (-3.2 to +2.3) | -1.2% (-4.6 to +2.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 14.3 | +14.3 (+11.5 to +17.2) | +12.3 (+4.74 to +19.9) | +14 (+4.06 to +23.9) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 128 to 512 (7 trials, 3 allowed, 3 refused); acting: 128 to 512 (6 trials, 3 allowed, 3 refused); acting: 256 to 512 (9 trials, 2 allowed, 3 refused); run B: acting: 128 to 512 (6 trials, 3 allowed, 3 refused); acting: 128 to 512 (7 trials, 3 allowed, 3 refused); acting: 128 to 512 (5 trials, 3 allowed, 2 refused); run C: acting: 512 to 640 (13 trials, 1 allowed, 4 refused); left native (13 trials, 0 allowed, 4 refused); acting: 512 to 640 (12 trials, 1 allowed, 4 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 186.4 | 191.6 | +2.8% (-24.2 to +29.8) | +0.9% (-64.5 to +66.3) | +0 (+0 to +0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 986.2 | 987.4 | +0.1% (-0.2 to +0.5) | -0.2% (-0.9 to +0.6) | -0.1% (-0.8 to +0.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| queries a second | 986.2 | 987.4 | +0.1% (-0.2 to +0.5) | -0.2% (-0.9 to +0.6) | -0.1% (-0.8 to +0.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 79.5 | 80.7 | +1.5% (-75.0 to +78.0) | +2.7% (-37.3 to +42.6) | -1.5% (-22.7 to +19.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 205.9 | 184.1 | -10.6% (-82.4 to +61.2) | +29.7% (-195.3 to +254.7) | -34.2% (-229.0 to +160.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 12.1 | 11.5 | -5.1% (-78.9 to +68.6) | +16.8% (-5.2 to +38.9) | -3.6% (-27.5 to +20.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 369.3 | -27.9% (-32.4 to -23.3) | -8.2% (-25.8 to +9.5) | -0.4% (-11.9 to +11.1) | STEADY, no difference beyond the noise (2 of 3 runs) |
| pages holding data, mean (MB) | 453.9 | 312.4 | -31.2% (-41.3 to -21.0) | -12.8% (-31.1 to +5.5) | -1.8% (-12.8 to +9.2) | STEADY, no difference beyond the noise (2 of 3 runs) |
| pages read from disk into the pool (misses) | 190,231 | 292,178 | +53.6% (+43.5 to +63.7) | +18.9% (-13.0 to +50.9) | +0.5% (-16.9 to +17.9) | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.142 | +2.6% (-11.5 to +16.8) | -0.1% (-13.4 to +13.2) | -0.9% (-10.7 to +8.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 244.3 | 250.7 | +2.6% (-12.0 to +17.2) | -0.2% (-14.0 to +13.6) | -0.9% (-10.5 to +8.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 2.95 | 2.89 | -1.9% (-48.5 to +44.6) | -7.3% (-97.4 to +82.8) | -0.9% (-10.5 to +8.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 13.0 | +13 (+3.06 to +22.9) | +18.7 (+12.4 to +24.9) | +12.7 (+11.2 to +14.1) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 128 to 512 (5 trials, 3 allowed, 2 refused); acting: 128 to 512 (9 trials, 3 allowed, 3 refused); acting: 128 to 512 (6 trials, 3 allowed, 3 refused); run B: acting: 384 to 512 (10 trials, 1 allowed, 3 refused); acting: 128 to 512 (9 trials, 3 allowed, 4 refused); acting: 384 to 640 (12 trials, 2 allowed, 2 refused); run C: left native (16 trials, 0 allowed, 3 refused); left native (17 trials, 0 allowed, 3 refused); acting: 384 to 512 (15 trials, 1 allowed, 4 refused).

**Across 4 untouched workloads: 0 gauge-rows GAIN in all three of our runs, 0 LOSS, 0 power given, 47 STEADY, 1 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
