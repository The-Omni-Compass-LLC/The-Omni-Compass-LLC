# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **STEADY, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40105173842 | `1aa4ebd3855c` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |
| B | 40107551073 | `1aa4ebd3855c` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |
| C | 40134818204 | `7743f2e82851` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,959 | 2,958 | -0.0% (-0.2 to +0.2) | +0.0% (-0.2 to +0.2) | +0.1% (-0.3 to +0.4) | STEADY, under the floor (the three runs' mean 0.01%) |
| throughput (transactions a second) | 2,965 | 2,965 | +0.0% (-0.1 to +0.1) | +0.0% (-0.2 to +0.2) | -0.0% (-0.2 to +0.1) | STEADY, under the floor (the three runs' mean 0.01%) |
| queries a second | 2,965 | 2,965 | +0.0% (-0.1 to +0.1) | +0.0% (-0.2 to +0.2) | -0.0% (-0.2 to +0.1) | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms) | 0.197 | 0.2 | +1.9% (-15.7 to +19.4) | -1.8% (-6.3 to +2.7) | -2.9% (-9.5 to +3.8) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.338 | 0.336 | -0.6% (-18.4 to +17.2) | -2.3% (-4.8 to +0.2) | -2.4% (-5.2 to +0.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.0941 | 0.0936 | -0.5% (-27.7 to +26.8) | +0.2% (-1.1 to +1.5) | -36.3% (-163.9 to +91.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 534.2 | +4.3% (-16.0 to +24.7) | -3.4% (-74.0 to +67.1) | -20.2% (-41.8 to +1.4) | **the runs disagree** |
| pages holding data, mean (MB) | 463.6 | 486.3 | +4.9% (-16.4 to +26.2) | -5.1% (-72.4 to +62.1) | -19.3% (-39.1 to +0.5) | **the runs disagree** |
| pages read from disk into the pool (misses) | 367,601 | 331,555 | -9.8% (-42.9 to +23.3) | +8.0% (-99.0 to +115.0) | +34.6% (-10.1 to +79.3) | shown, not judged |
| host CPU busy (share of the run) | 0.0736 | 0.0691 | -6.1% (-30.0 to +17.9) | +0.9% (-0.7 to +2.4) | -1.3% (-7.3 to +4.6) | **the runs disagree** |
| host CPU-seconds | 131.9 | 123.9 | -6.1% (-30.0 to +17.9) | +1.0% (-0.7 to +2.6) | -1.3% (-7.3 to +4.6) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.0979 | 0.092 | -6.0% (-30.1 to +18.0) | +1.0% (-0.7 to +2.7) | -1.4% (-7.4 to +4.6) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 10.0 | +10 (+0.0626 to +19.9) | +11.3 (+1.29 to +21.4) | +4.33 (-1.4 to +10.1) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 640 (6 trials, 2 allowed, 3 refused); acting: 512 to 768 (8 trials, 2 allowed, 3 refused); left native (4 trials, 0 allowed, 3 refused); run B: acting: 384 to 512 (8 trials, 1 allowed, 2 refused); acting: 384 to 512 (3 trials, 1 allowed, 2 refused); acting: 512 to 896 (7 trials, 3 allowed, 1 refused); run C: acting: 384 to 640 (4 trials, 2 allowed, 1 refused); acting: 384 to 512 (2 trials, 1 allowed, 1 refused); acting: 384 to 512 (2 trials, 1 allowed, 1 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292.8 | 293.4 | +0.2% (-1.5 to +2.0) | +0.2% (-0.3 to +0.6) | -0.1% (-1.9 to +1.8) | STEADY, under the floor (the three runs' mean 0.11%) |
| throughput (transactions a second) | 293.7 | 294.1 | +0.1% (-1.5 to +1.7) | +0.2% (-0.3 to +0.6) | +0.0% (-1.7 to +1.7) | STEADY, under the floor (the three runs' mean 0.10%) |
| queries a second | 4,700 | 4,705 | +0.1% (-1.5 to +1.7) | +0.2% (-0.3 to +0.6) | +0.0% (-1.7 to +1.7) | STEADY, under the floor (the three runs' mean 0.10%) |
| latency, 95th percentile (ms) | 5.12 | 5 | -2.4% (-11.6 to +6.8) | -1.2% (-6.4 to +4.0) | +0.0% (-4.5 to +4.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 7.04 | 6.83 | -2.9% (-14.0 to +8.1) | +0.0% (-4.5 to +4.5) | +1.2% (-4.1 to +6.6) | **the runs disagree** |
| latency, mean (ms) | 3.3 | 3.28 | -0.4% (-3.2 to +2.3) | -0.1% (-0.9 to +0.7) | -0.0% (-2.0 to +2.0) | STEADY, under the floor (the three runs' mean 0.17%) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 500.4 | -2.3% (-19.4 to +14.8) | -4.6% (-10.7 to +1.5) | +3.2% (-10.5 to +16.9) | **the runs disagree** |
| pages holding data, mean (MB) | 447.0 | 417.3 | -6.6% (-31.4 to +18.1) | -8.3% (-20.9 to +4.3) | -0.6% (-23.1 to +21.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read from disk into the pool (misses) | 245,765 | 245,551 | -0.1% (-33.3 to +33.2) | +0.1% (-15.9 to +16.1) | -4.6% (-30.1 to +20.8) | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.194 | +2.1% (-0.7 to +5.0) | +0.7% (-1.7 to +3.1) | +2.1% (-3.4 to +7.5) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 104.4 | 107.0 | +2.4% (-0.5 to +5.4) | +0.7% (-1.8 to +3.2) | +2.4% (-3.2 to +8.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.38 | +2.2% (+1.0 to +3.4) | +0.5% (-2.3 to +3.3) | +2.3% (-1.5 to +6.1) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 7 | +7 (+4.52 to +9.48) | +6 (-0.573 to +12.6) | +7.33 (+4.46 to +10.2) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 512 to 640 (6 trials, 1 allowed, 0 refused); acting: 384 to 512 (4 trials, 1 allowed, 1 refused); left native (4 trials, 0 allowed, 1 refused); run B: left native (4 trials, 0 allowed, 1 refused); acting: 384 to 512 (5 trials, 1 allowed, 1 refused); acting: 384 to 640 (5 trials, 2 allowed, 0 refused); run C: acting: 512 to 640 (6 trials, 1 allowed, 0 refused); left native (4 trials, 0 allowed, 1 refused); acting: 512 to 640 (7 trials, 1 allowed, 0 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294.4 | 295.0 | +0.2% (-0.4 to +0.8) | -0.2% (-1.2 to +0.7) | +0.0% (-1.3 to +1.3) | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (transactions a second) | 294.7 | 295.4 | +0.2% (-0.3 to +0.8) | -0.2% (-1.2 to +0.8) | +0.0% (-1.3 to +1.3) | STEADY, under the floor (the three runs' mean 0.02%) |
| queries a second | 4,715 | 4,727 | +0.2% (-0.3 to +0.8) | -0.2% (-1.2 to +0.8) | +0.0% (-1.3 to +1.3) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 4.1 | 4.08 | -0.6% (-3.1 to +2.0) | -0.6% (-3.2 to +2.0) | -1.8% (-1.9 to -1.7) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, 99th percentile (ms) | 5.71 | 5.67 | -0.6% (-5.7 to +4.5) | +0.0% (-4.5 to +4.6) | -0.6% (-3.1 to +2.0) | STEADY, under the floor (the three runs' mean 0.40%) |
| latency, mean (ms) | 3.2 | 3.18 | -0.8% (-1.3 to -0.2) | -0.4% (-3.1 to +2.3) | -1.1% (-3.1 to +0.9) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 597.1 | +16.6% (-16.2 to +49.5) | +13.7% (-6.4 to +33.8) | +13.5% (-18.4 to +45.5) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pages holding data, mean (MB) | 462.0 | 502.8 | +8.8% (-14.9 to +32.6) | +9.4% (-11.5 to +30.4) | +8.4% (-12.5 to +29.3) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read from disk into the pool (misses) | 654,275 | 538,931 | -17.6% (-47.4 to +12.2) | -20.5% (-49.9 to +9.0) | -16.4% (-61.1 to +28.4) | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.189 | -0.5% (-2.3 to +1.4) | -0.8% (-5.4 to +3.9) | -1.0% (-5.9 to +4.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 314.8 | 313.4 | -0.4% (-2.2 to +1.4) | -0.7% (-5.6 to +4.2) | -0.9% (-6.0 to +4.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 2.34 | 2.32 | -0.7% (-2.2 to +0.9) | -0.5% (-6.0 to +5.0) | -1.0% (-4.8 to +2.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 18.7 | +18.7 (+8.32 to +29) | +16 (+11.7 to +20.3) | +18 (+11.4 to +24.6) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 1024 (14 trials, 5 allowed, 1 refused); left native (13 trials, 0 allowed, 4 refused); acting: 512 to 1024 (15 trials, 4 allowed, 2 refused); run B: acting: 384 to 768 (11 trials, 3 allowed, 2 refused); acting: 512 to 768 (16 trials, 2 allowed, 3 refused); acting: 512 to 768 (13 trials, 2 allowed, 2 refused); run C: acting: 384 to 640 (9 trials, 2 allowed, 5 refused); acting: 512 to 896 (14 trials, 3 allowed, 3 refused); acting: 512 to 768 (11 trials, 2 allowed, 2 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 188.7 | 189.5 | +0.4% (-1.6 to +2.5) | -0.7% (-3.8 to +2.4) | +0.4% (-0.9 to +1.6) | STEADY, under the floor (the three runs' mean 0.04%) |
| throughput (transactions a second) | 196.5 | 196.1 | -0.2% (-1.0 to +0.5) | +0.1% (-1.7 to +2.0) | +0.0% (-1.2 to +1.3) | STEADY, under the floor (the three runs' mean 0.02%) |
| queries a second | 3,931 | 3,922 | -0.2% (-1.0 to +0.5) | +0.1% (-1.7 to +2.0) | +0.0% (-1.2 to +1.3) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 10.2 | 9.5 | -6.4% (-16.4 to +3.6) | +15.1% (-26.9 to +57.2) | -3.5% (-7.9 to +0.8) | **the runs disagree** |
| latency, 99th percentile (ms) | 15.2 | 15.9 | +4.4% (-59.8 to +68.5) | +57.0% (-70.3 to +184.2) | -4.1% (-13.3 to +5.0) | **the runs disagree** |
| latency, mean (ms) | 5.78 | 5.79 | +0.3% (-14.2 to +14.8) | +10.7% (-27.0 to +48.3) | -0.3% (-3.2 to +2.5) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 672.0 | +31.3% (-19.3 to +81.8) | +2.2% (-14.4 to +18.7) | +27.8% (+7.3 to +48.3) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pages holding data, mean (MB) | 461.1 | 565.7 | +22.7% (-5.5 to +50.8) | +2.3% (-11.4 to +16.0) | +20.7% (+1.8 to +39.6) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read from disk into the pool (misses) | 617,087 | 410,181 | -33.5% (-76.0 to +9.0) | -1.9% (-34.1 to +30.3) | -29.1% (-57.2 to -1.0) | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.214 | -3.1% (-5.2 to -1.0) | +2.4% (-1.5 to +6.3) | +0.7% (-2.5 to +3.9) | **the runs disagree** |
| host CPU-seconds | 354.6 | 343.9 | -3.0% (-4.8 to -1.3) | +2.5% (-1.3 to +6.2) | +0.9% (-2.1 to +4.0) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 4.1 | 3.96 | -3.4% (-3.7 to -3.1) | +3.1% (-2.8 to +9.1) | +0.5% (-2.7 to +3.8) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 18.3 | +18.3 (+5.83 to +30.8) | +14 (+5.04 to +23) | +23 (+18.7 to +27.3) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 512 to 896 (16 trials, 3 allowed, 3 refused); acting: 512 to 640 (14 trials, 1 allowed, 3 refused); acting: 512 to 1152 (14 trials, 5 allowed, 2 refused); run B: acting: 384 to 640 (7 trials, 2 allowed, 3 refused); acting: 512 to 640 (8 trials, 1 allowed, 4 refused); acting: 384 to 640 (7 trials, 2 allowed, 3 refused); run C: acting: 512 to 768 (14 trials, 2 allowed, 2 refused); acting: 384 to 896 (15 trials, 4 allowed, 3 refused); acting: 512 to 1024 (14 trials, 4 allowed, 3 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 148.1 | 144.4 | -2.5% (-71.3 to +66.4) | -22.9% (-69.5 to +23.6) | -21.7% (-177.1 to +133.7) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 986.3 | 986.6 | +0.0% (-1.0 to +1.1) | +0.0% (-0.1 to +0.2) | -0.0% (-0.6 to +0.5) | STEADY, under the floor (the three runs' mean 0.02%) |
| queries a second | 986.3 | 986.6 | +0.0% (-1.0 to +1.1) | +0.0% (-0.1 to +0.2) | -0.0% (-0.6 to +0.5) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 88.6 | 96.7 | +9.2% (-47.8 to +66.2) | +6.1% (-49.8 to +61.9) | +8.0% (-31.1 to +47.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 203.1 | 212.7 | +4.7% (-38.5 to +48.0) | +15.0% (-38.3 to +68.3) | +9.0% (-22.0 to +40.0) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 15.7 | 17.1 | +8.4% (-79.4 to +96.3) | +13.7% (-19.0 to +46.5) | +3.6% (-14.6 to +21.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 468.5 | -8.5% (-33.2 to +16.2) | -9.9% (-38.1 to +18.2) | +10.3% (-12.5 to +33.0) | **the runs disagree** |
| pages holding data, mean (MB) | 453.5 | 405.5 | -10.6% (-34.7 to +13.5) | -11.0% (-39.5 to +17.6) | +2.3% (-9.7 to +14.3) | **the runs disagree** |
| pages read from disk into the pool (misses) | 189,990 | 222,233 | +17.0% (-17.6 to +51.5) | +15.1% (-17.6 to +47.8) | -0.4% (-16.4 to +15.6) | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.134 | -0.1% (-20.7 to +20.6) | +7.0% (-14.5 to +28.4) | +39.3% (-83.9 to +162.5) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 237.7 | 237.7 | +0.0% (-20.2 to +20.3) | +6.9% (-14.2 to +28.1) | +39.8% (-84.4 to +163.9) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 3.84 | 3.61 | -6.0% (-107.1 to +95.2) | +46.7% (-86.8 to +180.1) | +68.3% (-132.1 to +268.7) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 16.0 | +16 (+4.62 to +27.4) | +12.7 (+6.41 to +18.9) | +22.7 (+8.98 to +36.3) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 512 (10 trials, 1 allowed, 5 refused); acting: 256 to 768 (8 trials, 4 allowed, 1 refused); acting: 512 to 768 (9 trials, 2 allowed, 2 refused); run B: acting: 384 to 640 (8 trials, 2 allowed, 4 refused); acting: 384 to 768 (9 trials, 3 allowed, 3 refused); acting: 384 to 512 (5 trials, 1 allowed, 3 refused); run C: left native (15 trials, 0 allowed, 3 refused); acting: 512 to 640 (16 trials, 1 allowed, 3 refused); acting: 384 to 1024 (16 trials, 5 allowed, 2 refused).

**Across 4 untouched workloads: 7 gauge-rows GAIN, 5 LOSS, 9 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 17 STEADY, 10 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
