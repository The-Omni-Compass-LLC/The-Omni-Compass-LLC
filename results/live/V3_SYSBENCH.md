# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number (a resource spent that rose reads **power given**, never a loss; the key: `docs/HOW_TO_READ_THE_RESULTS.md`)); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any increase in any run is marked. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38054765202 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |
| B | 38054768832 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |
| C | 38054773573 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,951 | 2,948 | -0.1% (-0.2 to +0.0) | +0.1% (-0.4 to +0.6) | -0.1% (-0.5 to +0.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 2,953 | 2,952 | -0.1% (-0.3 to +0.1) | +0.2% (-0.0 to +0.4) | -0.0% (-0.5 to +0.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| queries a second | 2,953 | 2,952 | -0.1% (-0.3 to +0.1) | +0.2% (-0.0 to +0.4) | -0.0% (-0.5 to +0.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.316 | 0.322 | +1.8% (-7.2 to +10.8) | +8.9% (-36.8 to +54.5) | -2.4% (-9.3 to +4.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.44 | 0.437 | -0.6% (-5.8 to +4.6) | +1.9% (-22.6 to +26.3) | -1.9% (-10.8 to +7.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.193 | 0.198 | +2.5% (-1.9 to +6.9) | -45.8% (-222.1 to +130.6) | -0.1% (-4.9 to +4.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 416.2 | -18.7% (-34.4 to -3.0) | -19.0% (-59.8 to +21.8) | -12.0% (-21.5 to -2.6) | STEADY, no difference beyond the noise (1 of 3 runs) |
| pages holding data, mean (MB) | 463.4 | 376.2 | -18.8% (-35.0 to -2.6) | -19.3% (-60.7 to +22.0) | -12.4% (-21.7 to -3.1) | STEADY, no difference beyond the noise (1 of 3 runs) |
| pages read from disk into the pool (misses) | 367,026 | 509,779 | +38.9% (+9.7 to +68.1) | +36.7% (-51.5 to +124.9) | +23.9% (-7.1 to +54.9) | shown, not judged |
| host CPU busy (share of the run) | 0.0937 | 0.0994 | +6.1% (-3.2 to +15.4) | +1.0% (-15.3 to +17.3) | +0.8% (-8.2 to +9.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 155.0 | 164.9 | +6.4% (-3.1 to +15.8) | +0.9% (-15.2 to +17.1) | +1.0% (-8.0 to +9.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.115 | 0.122 | +6.5% (-2.9 to +15.8) | +0.8% (-15.5 to +17.2) | +1.0% (-7.5 to +9.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 12.0 | +12 (-3.51 to +27.5) | +13.3 (+10.5 to +16.2) | +11.7 (+5.41 to +17.9) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 128 to 512 (4 trials, 3 allowed, 1 refused); acting: 128 to 512 (7 trials, 3 allowed, 4 refused); acting: 256 to 512 (6 trials, 2 allowed, 2 refused); run B: acting: 128 to 512 (6 trials, 3 allowed, 3 refused); acting: 256 to 512 (7 trials, 2 allowed, 2 refused); acting: 384 to 512 (8 trials, 1 allowed, 4 refused); run C: acting: 256 to 512 (6 trials, 2 allowed, 2 refused); acting: 256 to 512 (7 trials, 2 allowed, 3 refused); acting: 256 to 512 (8 trials, 2 allowed, 4 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292.9 | 293.6 | +0.2% (-0.6 to +1.1) | +0.1% (-1.7 to +2.0) | -0.0% (-1.6 to +1.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 293.6 | 294.2 | +0.2% (-0.4 to +0.8) | +0.2% (-1.7 to +2.0) | -0.2% (-2.4 to +2.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| queries a second | 4,697 | 4,707 | +0.2% (-0.4 to +0.8) | +0.2% (-1.7 to +2.0) | -0.2% (-2.4 to +2.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 5.12 | 5 | -2.4% (-11.7 to +6.9) | -0.6% (-7.4 to +6.2) | -2.9% (-15.6 to +9.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 7 | 6.91 | -1.2% (-8.0 to +5.6) | +0.6% (-6.2 to +7.4) | -55.5% (-418.7 to +307.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 3.25 | 3.27 | +0.7% (-3.1 to +4.6) | +0.0% (-1.8 to +1.9) | -28.4% (-142.3 to +85.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 484.1 | -5.5% (-13.3 to +2.4) | -9.1% (-20.1 to +2.0) | -44.8% (-71.8 to -17.8) | STEADY, no difference beyond the noise (2 of 3 runs) |
| pages holding data, mean (MB) | 447.4 | 413.7 | -7.5% (-23.8 to +8.8) | -13.6% (-22.2 to -5.0) | -44.7% (-74.5 to -14.8) | STEADY, no difference beyond the noise (1 of 3 runs) |
| pages read from disk into the pool (misses) | 243,343 | 243,156 | -0.1% (-10.3 to +10.2) | +5.6% (-10.6 to +21.8) | +49.0% (-13.9 to +112.0) | shown, not judged |
| host CPU busy (share of the run) | 0.185 | 0.19 | +2.3% (-4.1 to +8.7) | +2.2% (+0.9 to +3.5) | -0.6% (-2.4 to +1.2) | STEADY, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 102.1 | 104.5 | +2.4% (-4.2 to +9.0) | +2.6% (+0.7 to +4.4) | -0.6% (-2.4 to +1.3) | STEADY, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 2.28 | 2.33 | +2.2% (-4.5 to +9.0) | +2.3% (+0.3 to +4.3) | -0.5% (-2.5 to +1.4) | STEADY, no difference beyond the noise (2 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 7.67 | +7.67 (+0.495 to +14.8) | +7 (+2.7 to +11.3) | +4.67 (+0.872 to +8.46) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (7 trials, 1 allowed, 2 refused); left native (5 trials, 0 allowed, 1 refused); acting: 384 to 512 (7 trials, 1 allowed, 2 refused); run B: acting: 256 to 512 (7 trials, 2 allowed, 2 refused); left native (6 trials, 0 allowed, 1 refused); acting: 384 to 512 (5 trials, 1 allowed, 1 refused); run C: acting: 256 to 512 (4 trials, 2 allowed, 0 refused); acting: 256 to 640 (7 trials, 3 allowed, 0 refused); acting: 256 to 512 (6 trials, 2 allowed, 0 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295.1 | 293.8 | -0.5% (-0.8 to -0.1) | +0.1% (-1.0 to +1.1) | -0.3% (-1.8 to +1.3) | STEADY, no difference beyond the noise (2 of 3 runs) |
| throughput (transactions a second) | 295.5 | 294.2 | -0.4% (-0.9 to +0.1) | +0.1% (-1.0 to +1.1) | -0.3% (-1.8 to +1.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| queries a second | 4,728 | 4,708 | -0.4% (-0.9 to +0.1) | +0.1% (-1.0 to +1.1) | -0.3% (-1.8 to +1.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 4.23 | 4.18 | -1.2% (-3.8 to +1.4) | -1.2% (-3.8 to +1.4) | -3.0% (-16.8 to +10.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 6.13 | 6.06 | -1.2% (-8.0 to +5.6) | -1.2% (-8.0 to +5.6) | +1.1% (-5.7 to +8.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 3.2 | 3.19 | -0.5% (-2.8 to +1.8) | -0.4% (-1.2 to +0.5) | -0.8% (-5.9 to +4.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 517.3 | +1.0% (-24.8 to +26.9) | -40.4% (-44.3 to -36.5) | -24.8% (-31.1 to -18.5) | STEADY, no difference beyond the noise (1 of 3 runs) |
| pages holding data, mean (MB) | 461.8 | 463.4 | +0.4% (-25.7 to +26.4) | -38.7% (-43.7 to -33.6) | -22.2% (-26.9 to -17.5) | STEADY, no difference beyond the noise (1 of 3 runs) |
| pages read from disk into the pool (misses) | 655,923 | 616,884 | -6.0% (-49.4 to +37.5) | +97.2% (+81.1 to +113.3) | +61.0% (+29.3 to +92.8) | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.189 | -0.8% (-3.7 to +2.2) | -0.2% (-1.7 to +1.2) | -0.2% (-4.3 to +3.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 314.2 | 312.2 | -0.6% (-3.4 to +2.1) | -0.3% (-1.8 to +1.3) | -0.2% (-4.3 to +3.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.32 | -0.2% (-2.5 to +2.2) | -0.3% (-1.7 to +1.1) | +0.0% (-5.1 to +5.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 18.3 | +18.3 (+13.2 to +23.5) | +10.3 (-0.00979 to +20.7) | +8.67 (+4.87 to +12.5) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (13 trials, 1 allowed, 4 refused); acting: 512 to 640 (15 trials, 1 allowed, 4 refused); acting: 384 to 512 (14 trials, 1 allowed, 5 refused); run B: acting: 128 to 512 (8 trials, 3 allowed, 3 refused); acting: 256 to 512 (5 trials, 2 allowed, 1 refused); acting: 256 to 512 (7 trials, 2 allowed, 1 refused); run C: acting: 256 to 512 (5 trials, 2 allowed, 1 refused); acting: 256 to 640 (7 trials, 3 allowed, 1 refused); acting: 256 to 512 (6 trials, 2 allowed, 2 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192.4 | 190.9 | -0.8% (-1.3 to -0.3) | -0.3% (-1.7 to +1.1) | -0.9% (-2.6 to +0.9) | STEADY, no difference beyond the noise (2 of 3 runs) |
| throughput (transactions a second) | 197.1 | 196.2 | -0.5% (-1.3 to +0.4) | -0.3% (-1.4 to +0.9) | -0.3% (-1.8 to +1.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| queries a second | 3,943 | 3,925 | -0.5% (-1.3 to +0.4) | -0.3% (-1.4 to +0.9) | -0.3% (-1.8 to +1.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 8.58 | 8.95 | +4.3% (-1.0 to +9.5) | +1.2% (-1.4 to +3.8) | +6.2% (+0.9 to +11.5) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 13.2 | 13.4 | +1.2% (-1.4 to +3.8) | +0.5% (-6.1 to +7.2) | +4.3% (+1.5 to +7.1) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 5.28 | 5.32 | +0.7% (-0.0 to +1.5) | +0.4% (-0.9 to +1.7) | +1.9% (-1.8 to +5.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 485.7 | -5.1% (-9.9 to -0.3) | +4.4% (-14.1 to +22.9) | -4.8% (-26.3 to +16.8) | STEADY, no difference beyond the noise (2 of 3 runs) |
| pages holding data, mean (MB) | 462.1 | 430.5 | -6.8% (-10.8 to -2.8) | +3.8% (-13.9 to +21.4) | -7.4% (-19.7 to +4.8) | STEADY, no difference beyond the noise (2 of 3 runs) |
| pages read from disk into the pool (misses) | 615,886 | 667,087 | +8.3% (-10.2 to +26.9) | -6.1% (-38.9 to +26.7) | +13.1% (-23.5 to +49.6) | shown, not judged |
| host CPU busy (share of the run) | 0.21 | 0.211 | +0.5% (-2.2 to +3.2) | -0.0% (-2.0 to +1.9) | +2.0% (-1.6 to +5.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 337.3 | 339.5 | +0.6% (-2.0 to +3.3) | +0.1% (-1.7 to +2.0) | +2.2% (-1.7 to +6.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 3.83 | 3.88 | +1.4% (-1.5 to +4.4) | +0.4% (-2.4 to +3.3) | +3.1% (-2.4 to +8.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 23.0 | +23 (+16.4 to +29.6) | +20.3 (+6.65 to +34) | +23.3 (+19.5 to +27.1) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (13 trials, 1 allowed, 5 refused); acting: 384 to 640 (14 trials, 2 allowed, 4 refused); acting: 256 to 640 (13 trials, 3 allowed, 4 refused); run B: acting: 512 to 640 (14 trials, 1 allowed, 4 refused); acting: 256 to 640 (15 trials, 3 allowed, 5 refused); acting: 256 to 640 (14 trials, 3 allowed, 5 refused); run C: acting: 384 to 768 (15 trials, 3 allowed, 5 refused); acting: 256 to 512 (13 trials, 2 allowed, 5 refused); acting: 384 to 512 (12 trials, 1 allowed, 4 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 93.0 | 88.0 | -5.4% (-95.4 to +84.6) | +11.8% (-42.1 to +65.7) | +0.0% (-248.6 to +248.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 988.2 | 984.3 | -0.4% (-1.5 to +0.7) | -0.2% (-0.5 to +0.1) | +0.0% (-0.4 to +0.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| queries a second | 988.2 | 984.3 | -0.4% (-1.5 to +0.7) | -0.2% (-0.5 to +0.1) | +0.0% (-0.4 to +0.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 186.9 | 284.9 | +52.4% (-239.2 to +344.1) | -2.6% (-17.4 to +12.3) | -2.9% (-9.7 to +3.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 533.7 | 830.4 | +55.6% (-394.6 to +505.9) | -0.6% (-11.0 to +9.8) | -1.8% (-9.5 to +5.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 38.8 | 57.8 | +48.9% (-280.6 to +378.5) | -1.5% (-9.3 to +6.2) | +3.3% (-20.2 to +26.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 440.3 | -14.0% (-24.7 to -3.3) | -1.1% (-33.2 to +31.0) | -26.4% (-46.4 to -6.4) | STEADY, no difference beyond the noise (1 of 3 runs) |
| pages holding data, mean (MB) | 453.4 | 360.1 | -20.6% (-35.9 to -5.3) | -3.8% (-39.7 to +32.2) | -30.5% (-51.4 to -9.6) | STEADY, no difference beyond the noise (1 of 3 runs) |
| pages read from disk into the pool (misses) | 190,418 | 253,477 | +33.1% (+10.8 to +55.5) | +8.1% (-54.3 to +70.4) | +51.0% (+30.1 to +71.9) | shown, not judged |
| host CPU busy (share of the run) | 0.133 | 0.128 | -3.1% (-24.9 to +18.8) | -4.5% (-35.1 to +26.1) | -1.1% (-9.8 to +7.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 235.9 | 228.5 | -3.2% (-26.3 to +20.0) | -4.3% (-34.4 to +25.8) | -1.1% (-9.9 to +7.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 5.64 | 5.94 | +5.3% (-101.2 to +111.8) | -18.5% (-110.5 to +73.6) | -17.6% (-84.0 to +48.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 23.3 | +23.3 (+18.2 to +28.5) | +17.3 (+1.36 to +33.3) | +19.3 (+6.58 to +32.1) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 128 to 512 (11 trials, 3 allowed, 4 refused); acting: 256 to 512 (12 trials, 2 allowed, 4 refused); acting: 128 to 512 (13 trials, 3 allowed, 5 refused); run B: left native (20 trials, 0 allowed, 4 refused); acting: 128 to 512 (13 trials, 3 allowed, 4 refused); acting: 512 to 640 (19 trials, 1 allowed, 3 refused); run C: acting: 128 to 512 (6 trials, 3 allowed, 2 refused); acting: 128 to 512 (8 trials, 3 allowed, 3 refused); acting: 256 to 512 (12 trials, 2 allowed, 4 refused).

**Across 4 untouched workloads: 0 gauge-rows GAIN, 0 LOSS, 0 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 48 STEADY, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
