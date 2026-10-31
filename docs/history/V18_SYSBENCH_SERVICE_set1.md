# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **STEADY, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40105162824 | `1aa4ebd3855c` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |
| B | 40105173842 | `1aa4ebd3855c` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |
| C | 40107551073 | `1aa4ebd3855c` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,949 | 2,947 | -0.1% (-0.2 to +0.0) | -0.0% (-0.2 to +0.2) | +0.0% (-0.2 to +0.2) | STEADY, under the floor (the three runs' mean 0.04%) |
| throughput (transactions a second) | 2,954 | 2,952 | -0.1% (-0.2 to +0.0) | +0.0% (-0.1 to +0.1) | +0.0% (-0.2 to +0.2) | STEADY, under the floor (the three runs' mean 0.03%) |
| queries a second | 2,954 | 2,952 | -0.1% (-0.2 to +0.0) | +0.0% (-0.1 to +0.1) | +0.0% (-0.2 to +0.2) | STEADY, under the floor (the three runs' mean 0.03%) |
| latency, 95th percentile (ms) | 0.318 | 0.316 | -0.6% (-3.3 to +2.1) | +1.9% (-15.7 to +19.4) | -1.8% (-6.3 to +2.7) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.453 | 0.448 | -1.2% (-3.7 to +1.4) | -0.6% (-18.4 to +17.2) | -2.3% (-4.8 to +0.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.198 | 0.198 | +0.3% (-0.4 to +1.0) | -0.5% (-27.7 to +26.8) | +0.2% (-1.1 to +1.5) | STEADY, under the floor (the three runs' mean 0.02%) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 503.8 | -1.6% (-16.5 to +13.3) | +4.3% (-16.0 to +24.7) | -3.4% (-74.0 to +67.1) | **the runs disagree** |
| pages holding data, mean (MB) | 463.8 | 453.9 | -2.1% (-10.3 to +6.0) | +4.9% (-16.4 to +26.2) | -5.1% (-72.4 to +62.1) | **the runs disagree** |
| pages read from disk into the pool (misses) | 367,346 | 381,577 | +3.9% (-13.2 to +21.0) | -9.8% (-42.9 to +23.3) | +8.0% (-99.0 to +115.0) | shown, not judged |
| host CPU busy (share of the run) | 0.0946 | 0.0963 | +1.7% (-0.5 to +4.0) | -6.1% (-30.0 to +17.9) | +0.9% (-0.7 to +2.4) | **the runs disagree** |
| host CPU-seconds | 156.5 | 159.5 | +1.9% (-0.4 to +4.3) | -6.1% (-30.0 to +17.9) | +1.0% (-0.7 to +2.6) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.116 | 0.118 | +2.0% (-0.2 to +4.3) | -6.0% (-30.1 to +18.0) | +1.0% (-0.7 to +2.7) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 11.0 | +11 (+6.03 to +16) | +10 (+0.0626 to +19.9) | +11.3 (+1.29 to +21.4) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 768 (7 trials, 3 allowed, 1 refused); acting: 384 to 640 (7 trials, 2 allowed, 3 refused); acting: 256 to 640 (6 trials, 3 allowed, 1 refused); run B: acting: 384 to 640 (6 trials, 2 allowed, 3 refused); acting: 512 to 768 (8 trials, 2 allowed, 3 refused); left native (4 trials, 0 allowed, 3 refused); run C: acting: 384 to 512 (8 trials, 1 allowed, 2 refused); acting: 384 to 512 (3 trials, 1 allowed, 2 refused); acting: 512 to 896 (7 trials, 3 allowed, 1 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293.1 | 293.8 | +0.2% (-0.2 to +0.7) | +0.2% (-1.5 to +2.0) | +0.2% (-0.3 to +0.6) | STEADY, under the floor (the three runs' mean 0.20%) |
| throughput (transactions a second) | 294.2 | 295.2 | +0.3% (-0.3 to +0.9) | +0.1% (-1.5 to +1.7) | +0.2% (-0.3 to +0.6) | STEADY, under the floor (the three runs' mean 0.20%) |
| queries a second | 4,708 | 4,723 | +0.3% (-0.3 to +0.9) | +0.1% (-1.5 to +1.7) | +0.2% (-0.3 to +0.6) | STEADY, under the floor (the three runs' mean 0.20%) |
| latency, 95th percentile (ms) | 5.15 | 5.09 | -1.2% (-8.1 to +5.7) | -2.4% (-11.6 to +6.8) | -1.2% (-6.4 to +4.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 7.21 | 7.26 | +0.6% (-4.5 to +5.8) | -2.9% (-14.0 to +8.1) | +0.0% (-4.5 to +4.5) | **the runs disagree** |
| latency, mean (ms) | 3.33 | 3.32 | -0.2% (-3.6 to +3.1) | -0.4% (-3.2 to +2.3) | -0.1% (-0.9 to +0.7) | STEADY, under the floor (the three runs' mean 0.24%) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 554.1 | +8.2% (+1.8 to +14.6) | -2.3% (-19.4 to +14.8) | -4.6% (-10.7 to +1.5) | **the runs disagree** |
| pages holding data, mean (MB) | 450.8 | 486.5 | +7.9% (+3.8 to +12.0) | -6.6% (-31.4 to +18.1) | -8.3% (-20.9 to +4.3) | **the runs disagree** |
| pages read from disk into the pool (misses) | 245,212 | 213,586 | -12.9% (-16.2 to -9.5) | -0.1% (-33.3 to +33.2) | +0.1% (-15.9 to +16.1) | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.196 | +1.3% (-4.1 to +6.7) | +2.1% (-0.7 to +5.0) | +0.7% (-1.7 to +3.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 106.6 | 108.2 | +1.5% (-4.0 to +7.0) | +2.4% (-0.5 to +5.4) | +0.7% (-1.8 to +3.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 2.38 | 2.41 | +1.3% (-4.2 to +6.7) | +2.2% (+1.0 to +3.4) | +0.5% (-2.3 to +3.3) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 | +7.33 (+5.9 to +8.77) | +7 (+4.52 to +9.48) | +6 (-0.573 to +12.6) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 512 to 640 (7 trials, 1 allowed, 0 refused); acting: 512 to 640 (6 trials, 1 allowed, 0 refused); acting: 512 to 640 (7 trials, 1 allowed, 0 refused); run B: acting: 512 to 640 (6 trials, 1 allowed, 0 refused); acting: 384 to 512 (4 trials, 1 allowed, 1 refused); left native (4 trials, 0 allowed, 1 refused); run C: left native (4 trials, 0 allowed, 1 refused); acting: 384 to 512 (5 trials, 1 allowed, 1 refused); acting: 384 to 640 (5 trials, 2 allowed, 0 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290.5 | 292.7 | +0.8% (+0.5 to +1.0) | +0.2% (-0.4 to +0.8) | -0.2% (-1.2 to +0.7) | STEADY, under the floor (the three runs' mean 0.25%) |
| throughput (transactions a second) | 295.0 | 296.4 | +0.5% (+0.1 to +0.8) | +0.2% (-0.3 to +0.8) | -0.2% (-1.2 to +0.8) | STEADY, under the floor (the three runs' mean 0.17%) |
| queries a second | 4,720 | 4,742 | +0.5% (+0.1 to +0.8) | +0.2% (-0.3 to +0.8) | -0.2% (-1.2 to +0.8) | STEADY, under the floor (the three runs' mean 0.17%) |
| latency, 95th percentile (ms) | 2.71 | 2.68 | -1.2% (-3.7 to +1.4) | -0.6% (-3.1 to +2.0) | -0.6% (-3.2 to +2.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 27.6 | 21.3 | -22.8% (-132.7 to +87.1) | -0.6% (-5.7 to +4.5) | +0.0% (-4.5 to +4.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 3.14 | 2.86 | -8.9% (-54.1 to +36.3) | -0.8% (-1.3 to -0.2) | -0.4% (-3.1 to +2.3) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 514.8 | +0.5% (-60.7 to +61.8) | +16.6% (-16.2 to +49.5) | +13.7% (-6.4 to +33.8) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pages holding data, mean (MB) | 462.1 | 448.3 | -3.0% (-57.6 to +51.6) | +8.8% (-14.9 to +32.6) | +9.4% (-11.5 to +30.4) | **the runs disagree** |
| pages read from disk into the pool (misses) | 649,743 | 688,285 | +5.9% (-110.1 to +122.0) | -17.6% (-47.4 to +12.2) | -20.5% (-49.9 to +9.0) | shown, not judged |
| host CPU busy (share of the run) | 0.16 | 0.161 | +0.8% (-0.3 to +2.0) | -0.5% (-2.3 to +1.4) | -0.8% (-5.4 to +3.9) | **the runs disagree** |
| host CPU-seconds | 285.8 | 288.2 | +0.8% (-0.4 to +2.1) | -0.4% (-2.2 to +1.4) | -0.7% (-5.6 to +4.2) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 2.16 | 2.16 | +0.1% (-1.4 to +1.5) | -0.7% (-2.2 to +0.9) | -0.5% (-6.0 to +5.0) | STEADY, under the floor (the three runs' mean 0.37%) |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 | +10.3 (+7.46 to +13.2) | +18.7 (+8.32 to +29) | +16 (+11.7 to +20.3) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 512 to 768 (7 trials, 2 allowed, 1 refused); acting: 384 to 512 (5 trials, 1 allowed, 3 refused); acting: 512 to 640 (6 trials, 1 allowed, 4 refused); run B: acting: 384 to 1024 (14 trials, 5 allowed, 1 refused); left native (13 trials, 0 allowed, 4 refused); acting: 512 to 1024 (15 trials, 4 allowed, 2 refused); run C: acting: 384 to 768 (11 trials, 3 allowed, 2 refused); acting: 512 to 768 (16 trials, 2 allowed, 3 refused); acting: 512 to 768 (13 trials, 2 allowed, 2 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191.2 | 192.4 | +0.6% (-0.2 to +1.5) | +0.4% (-1.6 to +2.5) | -0.7% (-3.8 to +2.4) | **the runs disagree** |
| throughput (transactions a second) | 195.7 | 196.1 | +0.2% (-0.2 to +0.7) | -0.2% (-1.0 to +0.5) | +0.1% (-1.7 to +2.0) | STEADY, under the floor (the three runs' mean 0.04%) |
| queries a second | 3,913 | 3,922 | +0.2% (-0.2 to +0.7) | -0.2% (-1.0 to +0.5) | +0.1% (-1.7 to +2.0) | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, 95th percentile (ms) | 7 | 6.9 | -1.5% (-28.2 to +25.3) | -6.4% (-16.4 to +3.6) | +15.1% (-26.9 to +57.2) | **the runs disagree** |
| latency, 99th percentile (ms) | 125.8 | 71.4 | -43.3% (-131.7 to +45.2) | +4.4% (-59.8 to +68.5) | +57.0% (-70.3 to +184.2) | **the runs disagree** |
| latency, mean (ms) | 7.71 | 6.21 | -19.4% (-77.9 to +39.1) | +0.3% (-14.2 to +14.8) | +10.7% (-27.0 to +48.3) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 522.5 | +2.0% (-60.4 to +64.5) | +31.3% (-19.3 to +81.8) | +2.2% (-14.4 to +18.7) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pages holding data, mean (MB) | 460.9 | 457.2 | -0.8% (-56.2 to +54.5) | +22.7% (-5.5 to +50.8) | +2.3% (-11.4 to +16.0) | **the runs disagree** |
| pages read from disk into the pool (misses) | 614,694 | 660,359 | +7.4% (-82.4 to +97.3) | -33.5% (-76.0 to +9.0) | -1.9% (-34.1 to +30.3) | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.176 | +0.6% (-9.1 to +10.3) | -3.1% (-5.2 to -1.0) | +2.4% (-1.5 to +6.3) | **the runs disagree** |
| host CPU-seconds | 314.7 | 316.7 | +0.6% (-9.1 to +10.3) | -3.0% (-4.8 to -1.3) | +2.5% (-1.3 to +6.2) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 3.58 | 3.58 | +0.0% (-9.6 to +9.6) | -3.4% (-3.7 to -3.1) | +3.1% (-2.8 to +9.1) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 15.0 | +15 (+12.5 to +17.5) | +18.3 (+5.83 to +30.8) | +14 (+5.04 to +23) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 256 to 768 (9 trials, 4 allowed, 2 refused); acting: 256 to 640 (7 trials, 3 allowed, 3 refused); acting: 512 to 1024 (11 trials, 4 allowed, 2 refused); run B: acting: 512 to 896 (16 trials, 3 allowed, 3 refused); acting: 512 to 640 (14 trials, 1 allowed, 3 refused); acting: 512 to 1152 (14 trials, 5 allowed, 2 refused); run C: acting: 384 to 640 (7 trials, 2 allowed, 3 refused); acting: 512 to 640 (8 trials, 1 allowed, 4 refused); acting: 384 to 640 (7 trials, 2 allowed, 3 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 6.63 | 6.32 | -4.7% (-123.7 to +114.4) | -2.5% (-71.3 to +66.4) | -22.9% (-69.5 to +23.6) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 983.0 | 983.3 | +0.0% (-0.2 to +0.3) | +0.0% (-1.0 to +1.1) | +0.0% (-0.1 to +0.2) | STEADY, under the floor (the three runs' mean 0.04%) |
| queries a second | 983.0 | 983.3 | +0.0% (-0.2 to +0.3) | +0.0% (-1.0 to +1.1) | +0.0% (-0.1 to +0.2) | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, 95th percentile (ms) | 1.67 | 1.83 | +9.6% (-9.3 to +28.5) | +9.2% (-47.8 to +66.2) | +6.1% (-49.8 to +61.9) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 2.88 | 3.51 | +21.9% (-23.1 to +67.0) | +4.7% (-38.5 to +48.0) | +15.0% (-38.3 to +68.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 1.06 | 1.12 | +5.8% (-3.5 to +15.0) | +8.4% (-79.4 to +96.3) | +13.7% (-19.0 to +46.5) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 534.2 | +4.3% (-14.4 to +23.1) | -8.5% (-33.2 to +16.2) | -9.9% (-38.1 to +18.2) | **the runs disagree** |
| pages holding data, mean (MB) | 453.8 | 454.1 | +0.1% (-19.5 to +19.7) | -10.6% (-34.7 to +13.5) | -11.0% (-39.5 to +17.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read from disk into the pool (misses) | 189,677 | 192,914 | +1.7% (-19.9 to +23.3) | +17.0% (-17.6 to +51.5) | +15.1% (-17.6 to +47.8) | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.218 | +72.0% (-70.6 to +214.5) | -0.1% (-20.7 to +20.6) | +7.0% (-14.5 to +28.4) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 194.7 | 337.2 | +73.2% (-72.2 to +218.5) | +0.0% (-20.2 to +20.3) | +6.9% (-14.2 to +28.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 65.1 | 125.4 | +92.6% (-153.9 to +339.2) | -6.0% (-107.1 to +95.2) | +46.7% (-86.8 to +180.1) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 21.0 | +21 (+8.09 to +33.9) | +16 (+4.62 to +27.4) | +12.7 (+6.41 to +18.9) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 640 (13 trials, 2 allowed, 5 refused); left native (13 trials, 0 allowed, 3 refused); acting: 512 to 768 (18 trials, 2 allowed, 2 refused); run B: acting: 384 to 512 (10 trials, 1 allowed, 5 refused); acting: 256 to 768 (8 trials, 4 allowed, 1 refused); acting: 512 to 768 (9 trials, 2 allowed, 2 refused); run C: acting: 384 to 640 (8 trials, 2 allowed, 4 refused); acting: 384 to 768 (9 trials, 3 allowed, 3 refused); acting: 384 to 512 (5 trials, 1 allowed, 3 refused).

**Across 4 untouched workloads: 5 gauge-rows GAIN, 4 LOSS, 7 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 16 STEADY, 16 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
