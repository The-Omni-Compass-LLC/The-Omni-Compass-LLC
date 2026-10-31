# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **STEADY, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40235709142 | `5ce458c7e7d2` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |
| B | 40258018856 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |
| C | 40281464587 | `fa6da97bbaa6` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,942 | 2,945 | +0.1% (-0.2 to +0.4) | +0.0% (-0.2 to +0.2) | +0.0% (-0.1 to +0.2) | STEADY, under the floor (the three runs' mean 0.05%) |
| throughput (transactions a second) | 2,950 | 2,954 | +0.1% (-0.1 to +0.4) | +0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.1) | STEADY, under the floor (the three runs' mean 0.05%) |
| queries a second | 2,950 | 2,954 | +0.1% (-0.1 to +0.4) | +0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.1) | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms) | 0.351 | 0.344 | -1.8% (-11.4 to +7.8) | -2.5% (-11.8 to +6.8) | -19.9% (-50.8 to +11.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.481 | 0.473 | -1.7% (-10.2 to +6.9) | -1.2% (-6.6 to +4.1) | -9.8% (-25.2 to +5.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.214 | 0.213 | -0.4% (-9.3 to +8.5) | -5.5% (-126.1 to +115.0) | -6.1% (-33.7 to +21.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 486.2 | -5.0% (-6.1 to -4.0) | +1.5% (-24.1 to +27.0) | -12.1% (-46.8 to +22.6) | **the runs disagree** |
| pages holding data, mean (MB) | 463.7 | 441.2 | -4.8% (-8.6 to -1.0) | +0.4% (-23.9 to +24.7) | -11.3% (-50.2 to +27.6) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read from disk into the pool (misses) | 366,843 | 378,049 | +3.1% (+1.5 to +4.7) | -5.0% (-41.7 to +31.7) | +19.1% (-43.5 to +81.6) | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.112 | +0.0% (-13.6 to +13.7) | -0.5% (-12.0 to +11.0) | -5.5% (-38.9 to +28.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 186.4 | 186.6 | +0.1% (-13.6 to +13.9) | -0.4% (-11.7 to +10.9) | -5.4% (-38.7 to +27.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.139 | 0.139 | +0.0% (-13.9 to +14.0) | -0.4% (-11.7 to +10.8) | -5.4% (-38.5 to +27.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 6 | +6 (+1.03 to +11) | +11.3 (-2.35 to +25) | +8.67 (-0.058 to +17.4) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (4 trials, 1 allowed, 0 refused); acting: 384 to 512 (5 trials, 1 allowed, 0 refused); acting: 384 to 512 (6 trials, 1 allowed, 1 refused); run B: acting: 384 to 512 (5 trials, 1 allowed, 0 refused); acting: 384 to 512 (7 trials, 1 allowed, 1 refused); acting: 384 to 640 (10 trials, 2 allowed, 2 refused); run C: acting: 256 to 512 (4 trials, 2 allowed, 0 refused); acting: 256 to 512 (5 trials, 2 allowed, 2 refused); acting: 256 to 640 (7 trials, 3 allowed, 2 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294.4 | 295.4 | +0.3% (-1.8 to +2.5) | -0.3% (-1.4 to +0.8) | +0.5% (-1.5 to +2.5) | STEADY, under the floor (the three runs' mean 0.17%) |
| throughput (transactions a second) | 294.5 | 295.6 | +0.4% (-1.8 to +2.5) | -0.5% (-1.7 to +0.7) | +0.5% (-1.5 to +2.4) | STEADY, under the floor (the three runs' mean 0.12%) |
| queries a second | 4,712 | 4,730 | +0.4% (-1.8 to +2.5) | -0.5% (-1.7 to +0.7) | +0.5% (-1.5 to +2.4) | STEADY, under the floor (the three runs' mean 0.12%) |
| latency, 95th percentile (ms) | 2.77 | 2.73 | -1.3% (-12.9 to +10.3) | -1.8% (-9.6 to +6.0) | -3.5% (-11.1 to +4.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 4.36 | 4.33 | -0.6% (-3.0 to +1.9) | -4.1% (-9.1 to +0.9) | -4.1% (-10.8 to +2.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 1.33 | 1.33 | -0.4% (-12.4 to +11.7) | -0.4% (-1.6 to +0.8) | -0.2% (-3.1 to +2.8) | STEADY, under the floor (the three runs' mean 0.31%) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 421.1 | -17.8% (-21.7 to -13.8) | -14.8% (-15.1 to -14.4) | -16.8% (-22.9 to -10.6) | **GAIN in all three of our runs** |
| pages holding data, mean (MB) | 444.6 | 374.8 | -15.7% (-23.8 to -7.6) | -11.8% (-12.7 to -10.9) | -14.1% (-21.6 to -6.6) | **GAIN in all three of our runs** |
| pages read from disk into the pool (misses) | 243,276 | 264,734 | +8.8% (+5.7 to +12.0) | +5.5% (+0.0 to +11.0) | +6.9% (+1.9 to +11.9) | shown, not judged |
| host CPU busy (share of the run) | 0.0992 | 0.0983 | -1.0% (-12.3 to +10.4) | -0.2% (-4.6 to +4.2) | +1.2% (-1.7 to +4.2) | **the runs disagree** |
| host CPU-seconds | 59.6 | 58.9 | -1.0% (-12.4 to +10.3) | -0.0% (-4.7 to +4.6) | +1.3% (-1.7 to +4.2) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 1.33 | 1.31 | -1.4% (-14.8 to +12.0) | +0.3% (-5.0 to +5.5) | +0.8% (-1.5 to +3.0) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 5.67 | +5.67 (+4.23 to +7.1) | +7 (+7 to +7) | +6 (+3.52 to +8.48) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 256 to 640 (4 trials, 3 allowed, 0 refused); acting: 384 to 512 (3 trials, 1 allowed, 1 refused); acting: 256 to 640 (4 trials, 3 allowed, 0 refused); run B: acting: 384 to 640 (4 trials, 2 allowed, 1 refused); acting: 384 to 640 (4 trials, 2 allowed, 1 refused); acting: 384 to 640 (4 trials, 2 allowed, 1 refused); run C: acting: 384 to 640 (4 trials, 2 allowed, 1 refused); acting: 384 to 512 (3 trials, 1 allowed, 1 refused); acting: 256 to 640 (4 trials, 3 allowed, 0 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294.1 | 293.5 | -0.2% (-0.7 to +0.3) | +0.4% (-0.7 to +1.6) | -0.0% (-1.6 to +1.6) | STEADY, under the floor (the three runs' mean 0.07%) |
| throughput (transactions a second) | 296.3 | 296.1 | -0.1% (-0.7 to +0.6) | +0.4% (-0.7 to +1.5) | +0.0% (-1.6 to +1.6) | STEADY, under the floor (the three runs' mean 0.12%) |
| queries a second | 4,741 | 4,738 | -0.1% (-0.7 to +0.6) | +0.4% (-0.7 to +1.5) | +0.0% (-1.6 to +1.6) | STEADY, under the floor (the three runs' mean 0.12%) |
| latency, 95th percentile (ms) | 2.81 | 2.73 | -2.9% (-9.6 to +3.7) | -1.8% (-6.2 to +2.6) | +0.6% (-2.0 to +3.2) | **the runs disagree** |
| latency, 99th percentile (ms) | 6.05 | 9.72 | +60.7% (-201.8 to +323.3) | -2.4% (-9.0 to +4.3) | -0.6% (-3.1 to +1.9) | **the runs disagree** |
| latency, mean (ms) | 2.4 | 2.49 | +3.9% (-26.2 to +34.1) | -0.1% (-1.4 to +1.1) | +0.4% (-0.6 to +1.4) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 457.5 | -10.7% (-28.7 to +7.3) | -10.0% (-27.5 to +7.6) | -22.2% (-32.0 to -12.3) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages holding data, mean (MB) | 462.0 | 426.2 | -7.7% (-31.5 to +16.0) | -7.8% (-25.9 to +10.2) | -21.4% (-34.3 to -8.5) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read from disk into the pool (misses) | 652,102 | 779,000 | +19.5% (-23.6 to +62.5) | +18.4% (-21.9 to +58.8) | +42.6% (+28.1 to +57.2) | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.163 | +0.1% (-6.3 to +6.5) | +1.5% (-0.1 to +3.0) | +2.0% (-0.2 to +4.3) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 291.2 | 291.5 | +0.1% (-6.2 to +6.4) | +1.7% (-0.1 to +3.4) | +2.4% (+0.0 to +4.7) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 2.17 | 2.18 | +0.3% (-6.3 to +6.9) | +1.2% (-1.2 to +3.6) | +2.4% (+0.5 to +4.2) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 | +12.3 (+4.74 to +19.9) | +12.3 (+9.46 to +15.2) | +9.67 (+6.8 to +12.5) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 256 to 512 (7 trials, 2 allowed, 0 refused); acting: 256 to 640 (8 trials, 3 allowed, 0 refused); acting: 256 to 640 (8 trials, 3 allowed, 1 refused); run B: acting: 256 to 640 (7 trials, 3 allowed, 1 refused); acting: 256 to 640 (7 trials, 3 allowed, 1 refused); acting: 256 to 512 (6 trials, 2 allowed, 1 refused); run C: acting: 256 to 512 (6 trials, 2 allowed, 1 refused); acting: 256 to 512 (6 trials, 2 allowed, 1 refused); acting: 256 to 512 (6 trials, 2 allowed, 1 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191.8 | 191.2 | -0.3% (-1.5 to +0.8) | -0.1% (-0.9 to +0.7) | +0.6% (-1.6 to +2.7) | STEADY, under the floor (the three runs' mean 0.06%) |
| throughput (transactions a second) | 196.4 | 196.0 | -0.2% (-0.7 to +0.3) | -0.2% (-1.1 to +0.6) | +0.6% (-1.3 to +2.4) | STEADY, under the floor (the three runs' mean 0.03%) |
| queries a second | 3,928 | 3,920 | -0.2% (-0.7 to +0.3) | -0.2% (-1.1 to +0.6) | +0.6% (-1.3 to +2.4) | STEADY, under the floor (the three runs' mean 0.03%) |
| latency, 95th percentile (ms) | 8.79 | 8.69 | -1.2% (-6.4 to +4.0) | -2.4% (-7.5 to +2.7) | -1.9% (-9.5 to +5.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 12.8 | 13.0 | +1.2% (-5.6 to +8.0) | -0.6% (-3.2 to +2.0) | -1.4% (-26.6 to +23.8) | **the runs disagree** |
| latency, mean (ms) | 5.46 | 5.44 | -0.4% (-2.4 to +1.7) | -0.7% (-3.1 to +1.7) | +0.7% (-6.3 to +7.6) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 509.9 | -0.4% (-3.9 to +3.1) | +6.7% (-15.4 to +28.8) | +6.6% (-10.0 to +23.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pages holding data, mean (MB) | 461.1 | 456.9 | -0.9% (-7.1 to +5.2) | +5.9% (-10.3 to +22.1) | +6.0% (-9.6 to +21.7) | **the runs disagree** |
| pages read from disk into the pool (misses) | 613,765 | 601,506 | -2.0% (-7.8 to +3.8) | -12.0% (-40.2 to +16.2) | -11.7% (-44.0 to +20.6) | shown, not judged |
| host CPU busy (share of the run) | 0.224 | 0.22 | -1.7% (-7.7 to +4.4) | -1.1% (-5.9 to +3.8) | -2.4% (-11.7 to +6.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 361.4 | 355.4 | -1.7% (-7.9 to +4.5) | -0.9% (-5.9 to +4.1) | -2.4% (-11.6 to +6.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 4.12 | 4.06 | -1.3% (-6.9 to +4.2) | -0.9% (-6.5 to +4.8) | -3.0% (-10.0 to +4.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 | +16.3 (+14.9 to +17.8) | +20.7 (+17.8 to +23.5) | +15.7 (+2.92 to +28.4) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (9 trials, 1 allowed, 3 refused); acting: 384 to 512 (11 trials, 1 allowed, 4 refused); acting: 384 to 512 (9 trials, 1 allowed, 3 refused); run B: acting: 384 to 640 (12 trials, 2 allowed, 3 refused); acting: 384 to 640 (11 trials, 2 allowed, 3 refused); acting: 384 to 512 (11 trials, 1 allowed, 4 refused); run C: acting: 512 to 640 (9 trials, 1 allowed, 2 refused); left native (8 trials, 0 allowed, 1 refused); acting: 384 to 640 (10 trials, 2 allowed, 2 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 391.7 | 395.2 | +0.9% (-11.3 to +13.1) | +196.6% (-172.3 to +565.4) | -1.7% (-41.9 to +38.5) | **the runs disagree** |
| throughput (transactions a second) | 988.9 | 989.8 | +0.1% (-0.2 to +0.4) | -0.0% (-0.3 to +0.3) | +0.0% (-0.3 to +0.3) | STEADY, under the floor (the three runs' mean 0.03%) |
| queries a second | 988.9 | 989.8 | +0.1% (-0.2 to +0.4) | -0.0% (-0.3 to +0.3) | +0.0% (-0.3 to +0.3) | STEADY, under the floor (the three runs' mean 0.03%) |
| latency, 95th percentile (ms) | 2.79 | 3.01 | +7.8% (-28.1 to +43.7) | -42.1% (-104.9 to +20.8) | -1.9% (-14.1 to +10.3) | **the runs disagree** |
| latency, 99th percentile (ms) | 5.6 | 8.22 | +46.7% (-75.0 to +168.4) | -45.2% (-90.4 to +0.0) | -1.6% (-26.6 to +23.5) | **the runs disagree** |
| latency, mean (ms) | 0.943 | 1.06 | +11.9% (-24.1 to +47.9) | -28.6% (-59.3 to +2.1) | -1.1% (-10.7 to +8.4) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 512.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| pages holding data, mean (MB) | 453.7 | 450.4 | -0.7% (-4.7 to +3.2) | -0.8% (-3.1 to +1.5) | -0.6% (-3.5 to +2.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read from disk into the pool (misses) | 189,380 | 187,151 | -1.2% (-5.2 to +2.8) | -1.1% (-4.9 to +2.7) | -1.3% (-6.6 to +4.0) | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.104 | -1.4% (-12.0 to +9.2) | -38.0% (-78.3 to +2.2) | -2.1% (-16.2 to +12.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 186.0 | 183.4 | -1.4% (-11.9 to +9.0) | -37.9% (-79.8 to +4.1) | -2.0% (-16.0 to +12.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 1.05 | 1.04 | -1.7% (-24.9 to +21.5) | -97.1% (-308.6 to +114.4) | -4.7% (-56.1 to +46.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (0 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run B: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run C: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused).

**Across 4 untouched workloads: 14 gauge-rows GAIN, 1 LOSS, 4 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 17 STEADY, 12 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
