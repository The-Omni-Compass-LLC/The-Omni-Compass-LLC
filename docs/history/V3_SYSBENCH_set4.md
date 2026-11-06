# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C confirmation

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **confirmed better** or **confirmed WORSE**; a run whose interval includes zero reads **no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any increase in any run is WORSE. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38013329351 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |
| B | 38013334121 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |
| C | 38013338730 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,945 | 2,945 | -0.0% (-0.2 to +0.2) | -0.1% (-0.4 to +0.2) | -0.0% (-0.2 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 2,954 | 2,952 | -0.1% (-0.1 to -0.0) | +0.0% (-0.6 to +0.6) | -0.0% (-0.2 to +0.2) | no difference beyond the noise (2 of 3 runs) |
| queries a second | 2,954 | 2,952 | -0.1% (-0.1 to -0.0) | +0.0% (-0.6 to +0.6) | -0.0% (-0.2 to +0.2) | no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 0.334 | 0.35 | +4.9% (-0.1 to +9.8) | +7.2% (-28.4 to +42.8) | -0.6% (-3.2 to +2.0) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.473 | 0.473 | +0.0% (-4.2 to +4.2) | +2.9% (-9.7 to +15.6) | +0.0% (+0.0 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.23 | 0.216 | -6.1% (-36.6 to +24.4) | +2.3% (-4.8 to +9.4) | +1.4% (-0.4 to +3.2) | no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 439.7 | -14.1% (-24.9 to -3.3) | -14.0% (-27.3 to -0.8) | -12.7% (-32.1 to +6.7) | no difference beyond the noise (1 of 3 runs) |
| pages holding data, mean (MB) | 463.4 | 398.5 | -14.0% (-20.2 to -7.8) | -13.1% (-25.4 to -0.8) | -12.2% (-30.5 to +6.1) | no difference beyond the noise (1 of 3 runs) |
| pages read from disk into the pool (misses) | 367,507 | 454,443 | +23.7% (+1.8 to +45.5) | +23.7% (-4.3 to +51.7) | +24.0% (-20.8 to +68.8) | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.116 | +13.0% (+7.9 to +18.1) | +2.5% (-6.8 to +11.7) | +3.0% (-0.2 to +6.2) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 169.8 | 192.4 | +13.4% (+7.9 to +18.8) | +2.4% (-6.5 to +11.3) | +3.2% (-0.3 to +6.7) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.126 | 0.143 | +13.4% (+7.9 to +18.9) | +2.5% (-6.2 to +11.2) | +3.2% (-0.3 to +6.8) | no difference beyond the noise (2 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 | +7.33 (+2.16 to +12.5) | +5 (+0.0313 to +9.97) | +5 (+0.0313 to +9.97) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 256 to 512 (15 trials, 2 allowed, 0 refused); acting: 256 to 512 (7 trials, 2 allowed, 0 refused); acting: 256 to 512 (8 trials, 2 allowed, 0 refused); run B: acting: 256 to 512 (6 trials, 2 allowed, 0 refused); acting: 256 to 512 (8 trials, 2 allowed, 0 refused); acting: 256 to 512 (9 trials, 2 allowed, 0 refused); run C: acting: 128 to 512 (6 trials, 3 allowed, 0 refused); acting: 256 to 512 (7 trials, 2 allowed, 0 refused); acting: 384 to 512 (11 trials, 1 allowed, 0 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293.9 | 292.9 | -0.3% (-2.1 to +1.4) | +0.7% (+0.4 to +1.1) | +0.0% (-0.5 to +0.5) | no difference beyond the noise (2 of 3 runs) |
| throughput (transactions a second) | 295.3 | 294.0 | -0.4% (-1.9 to +1.1) | +0.8% (+0.1 to +1.5) | +0.0% (-0.3 to +0.3) | no difference beyond the noise (2 of 3 runs) |
| queries a second | 4,724 | 4,704 | -0.4% (-1.9 to +1.1) | +0.8% (+0.1 to +1.5) | +0.0% (-0.3 to +0.3) | no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 5.37 | 5.31 | -1.2% (-13.9 to +11.6) | -0.0% (-7.8 to +7.8) | -1.8% (-6.1 to +2.6) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 7.48 | 7.3 | -2.3% (-20.6 to +15.9) | +0.0% (-13.5 to +13.5) | -0.6% (-7.3 to +6.1) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 3.44 | 3.46 | +0.8% (-2.7 to +4.4) | +1.1% (-1.0 to +3.2) | +0.2% (-2.2 to +2.7) | no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 495.1 | -3.3% (-10.2 to +3.6) | -1.9% (-4.8 to +1.0) | -44.9% (-68.3 to -21.4) | no difference beyond the noise (2 of 3 runs) |
| pages holding data, mean (MB) | 444.9 | 411.5 | -7.5% (-15.7 to +0.7) | -6.5% (-12.3 to -0.8) | -46.0% (-69.4 to -22.5) | no difference beyond the noise (1 of 3 runs) |
| pages read from disk into the pool (misses) | 243,617 | 250,676 | +2.9% (-5.5 to +11.3) | +0.6% (-2.4 to +3.7) | +51.8% (+0.2 to +103.3) | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.208 | +1.9% (+0.4 to +3.5) | +3.6% (-1.0 to +8.2) | +0.7% (-1.1 to +2.6) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 112.9 | 115.4 | +2.3% (+0.9 to +3.6) | +3.8% (-1.0 to +8.7) | +0.7% (-1.3 to +2.8) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 2.51 | 2.57 | +2.5% (+0.4 to +4.6) | +3.1% (-1.7 to +7.9) | +0.7% (-1.5 to +2.9) | no difference beyond the noise (2 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 3 | +3 (+0.516 to +5.48) | +5.33 (+2.46 to +8.2) | +4.33 (+1.46 to +7.2) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (8 trials, 0 allowed, 0 refused); acting: 384 to 512 (6 trials, 1 allowed, 0 refused); left native (8 trials, 0 allowed, 0 refused); run B: left native (9 trials, 0 allowed, 0 refused); left native (8 trials, 0 allowed, 0 refused); left native (9 trials, 0 allowed, 0 refused); run C: acting: 256 to 512 (5 trials, 2 allowed, 0 refused); acting: 256 to 512 (6 trials, 2 allowed, 0 refused); acting: 128 to 512 (3 trials, 3 allowed, 0 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294.8 | 294.6 | -0.1% (-0.2 to +0.1) | +0.1% (-0.2 to +0.4) | -0.3% (-0.4 to -0.1) | no difference beyond the noise (2 of 3 runs) |
| throughput (transactions a second) | 294.9 | 294.8 | -0.1% (-0.2 to +0.1) | +0.1% (-0.3 to +0.5) | -0.2% (-0.4 to -0.0) | no difference beyond the noise (2 of 3 runs) |
| queries a second | 4,719 | 4,716 | -0.1% (-0.2 to +0.1) | +0.1% (-0.3 to +0.5) | -0.2% (-0.4 to -0.0) | no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 4.15 | 4.08 | -1.8% (-6.3 to +2.7) | -1.8% (-6.2 to +2.7) | -2.9% (-7.9 to +2.0) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.54 | 5.47 | -1.2% (-8.1 to +5.7) | -1.2% (-7.9 to +5.6) | -1.2% (-10.2 to +7.9) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 3.24 | 3.22 | -0.6% (-3.9 to +2.7) | -0.0% (-2.5 to +2.4) | +0.5% (-1.5 to +2.5) | no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 443.2 | -13.4% (-40.7 to +13.8) | -12.7% (-41.0 to +15.6) | -32.0% (-45.4 to -18.7) | no difference beyond the noise (2 of 3 runs) |
| pages holding data, mean (MB) | 461.9 | 401.1 | -13.2% (-33.1 to +6.8) | -13.0% (-35.7 to +9.7) | -30.8% (-45.8 to -15.9) | no difference beyond the noise (2 of 3 runs) |
| pages read from disk into the pool (misses) | 653,814 | 826,435 | +26.4% (-32.6 to +85.4) | +29.1% (-37.5 to +95.8) | +84.0% (+52.3 to +115.7) | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.197 | -0.2% (-6.5 to +6.1) | +1.2% (-2.6 to +4.9) | +0.4% (-1.8 to +2.7) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 327.0 | 326.7 | -0.1% (-6.9 to +6.8) | +1.4% (-2.5 to +5.2) | +0.4% (-1.8 to +2.7) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 2.42 | 2.42 | -0.0% (-6.7 to +6.6) | +1.3% (-2.3 to +4.9) | +0.7% (-1.7 to +3.1) | no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 10.0 | +10 (+1.04 to +19) | +6.67 (+1.5 to +11.8) | +7 (+2.03 to +12) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (22 trials, 0 allowed, 0 refused); acting: 384 to 512 (17 trials, 1 allowed, 0 refused); acting: 384 to 512 (23 trials, 1 allowed, 0 refused); run B: acting: 256 to 512 (19 trials, 2 allowed, 0 refused); left native (18 trials, 0 allowed, 0 refused); acting: 384 to 512 (18 trials, 1 allowed, 0 refused); run C: acting: 128 to 512 (5 trials, 3 allowed, 0 refused); acting: 256 to 512 (10 trials, 2 allowed, 0 refused); acting: 256 to 512 (8 trials, 2 allowed, 0 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191.6 | 192.0 | +0.2% (-1.0 to +1.4) | -0.1% (-1.2 to +1.0) | -0.0% (-1.0 to +0.9) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 197.4 | 196.5 | -0.5% (-1.9 to +1.0) | +0.3% (-1.5 to +2.0) | +0.0% (-0.9 to +1.0) | no difference beyond the noise (3 of 3 runs) |
| queries a second | 3,948 | 3,930 | -0.5% (-1.9 to +1.0) | +0.3% (-1.5 to +2.0) | +0.0% (-0.9 to +1.0) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 8.58 | 7.63 | -11.1% (-79.9 to +57.7) | +2.3% (-18.8 to +23.3) | +6.2% (+1.0 to +11.4) | no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 38.0 | 30.3 | -20.2% (-91.0 to +50.7) | -19.5% (-165.0 to +126.0) | -17.1% (-40.7 to +6.4) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 4.79 | 4.71 | -1.6% (-35.8 to +32.6) | -9.3% (-69.0 to +50.3) | -1.3% (-15.9 to +13.2) | no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 410.2 | -19.9% (-36.9 to -2.8) | -9.6% (-18.8 to -0.3) | -15.8% (-27.0 to -4.7) | **confirmed better** |
| pages holding data, mean (MB) | 461.6 | 369.3 | -20.0% (-34.6 to -5.4) | -10.6% (-18.6 to -2.5) | -15.8% (-26.1 to -5.4) | **confirmed better** |
| pages read from disk into the pool (misses) | 614,990 | 881,367 | +43.3% (-10.7 to +97.4) | +18.9% (-16.1 to +54.0) | +34.5% (+2.4 to +66.7) | shown, not judged |
| host CPU busy (share of the run) | 0.185 | 0.19 | +2.4% (-0.7 to +5.6) | +2.0% (-1.7 to +5.7) | -0.2% (-2.0 to +1.6) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 328.6 | 336.5 | +2.4% (-0.7 to +5.5) | +2.0% (-1.6 to +5.7) | -0.2% (-2.0 to +1.6) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 3.76 | 3.85 | +2.2% (-1.4 to +5.7) | +2.1% (-2.5 to +6.7) | -0.1% (-2.5 to +2.2) | no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 13.3 | +13.3 (+7.6 to +19.1) | +12 (+9.52 to +14.5) | +12.3 (+6.08 to +18.6) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 256 to 512 (16 trials, 2 allowed, 0 refused); acting: 128 to 512 (12 trials, 3 allowed, 0 refused); acting: 128 to 512 (9 trials, 3 allowed, 0 refused); run B: acting: 384 to 512 (18 trials, 1 allowed, 0 refused); acting: 128 to 512 (15 trials, 3 allowed, 0 refused); acting: 256 to 512 (17 trials, 2 allowed, 0 refused); run C: acting: 256 to 512 (15 trials, 2 allowed, 0 refused); acting: 256 to 512 (13 trials, 2 allowed, 0 refused); acting: 128 to 512 (13 trials, 3 allowed, 0 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3.58 | 4.14 | +15.6% (-262.9 to +294.1) | -7.9% (-80.2 to +64.3) | +0.5% (-37.6 to +38.7) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 982.9 | 982.1 | -0.1% (-0.4 to +0.2) | -0.0% (-0.7 to +0.6) | -0.1% (-0.2 to +0.1) | no difference beyond the noise (3 of 3 runs) |
| queries a second | 982.9 | 982.1 | -0.1% (-0.4 to +0.2) | -0.0% (-0.7 to +0.6) | -0.1% (-0.2 to +0.1) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 1.87 | 1.88 | +0.5% (-16.8 to +17.8) | +4.8% (-7.8 to +17.4) | -9.3% (-18.1 to -0.5) | no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 3.54 | 3.53 | -0.3% (-38.3 to +37.8) | +0.5% (-16.4 to +17.3) | -1.8% (-15.1 to +11.5) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.23 | 1.19 | -3.2% (-64.5 to +58.2) | +0.9% (-5.6 to +7.3) | +3.6% (-33.8 to +41.0) | no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 485.4 | -5.2% (-23.6 to +13.3) | -18.2% (-20.4 to -16.0) | -33.3% (-53.2 to -13.4) | no difference beyond the noise (1 of 3 runs) |
| pages holding data, mean (MB) | 453.6 | 414.9 | -8.5% (-34.3 to +17.3) | -21.5% (-26.0 to -17.0) | -39.7% (-59.6 to -19.8) | no difference beyond the noise (1 of 3 runs) |
| pages read from disk into the pool (misses) | 189,157 | 212,034 | +12.1% (-38.3 to +62.5) | +35.7% (+32.4 to +39.0) | +59.6% (+36.6 to +82.7) | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.158 | +24.2% (-120.0 to +168.4) | +44.9% (-41.4 to +131.2) | +4.6% (-15.8 to +25.0) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 196.0 | 244.5 | +24.7% (-119.9 to +169.3) | +45.4% (-42.3 to +133.1) | +4.7% (-15.4 to +24.8) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 198.1 | 184.6 | -6.8% (-382.5 to +368.9) | +41.3% (-55.8 to +138.4) | -0.8% (-68.6 to +66.9) | no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 11.0 | +11 (-10.5 to +32.5) | +16.3 (+7.61 to +25.1) | +15.3 (+12.5 to +18.2) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (21 trials, 0 allowed, 0 refused); left native (22 trials, 0 allowed, 0 refused); acting: 128 to 512 (21 trials, 3 allowed, 0 refused); run B: acting: 128 to 512 (21 trials, 3 allowed, 0 refused); acting: 128 to 512 (17 trials, 3 allowed, 0 refused); acting: 128 to 512 (21 trials, 3 allowed, 0 refused); run C: acting: 128 to 512 (10 trials, 3 allowed, 0 refused); acting: 128 to 512 (8 trials, 3 allowed, 0 refused); acting: 128 to 512 (7 trials, 3 allowed, 0 refused).

**Across 4 untouched workloads: 2 gauge-rows confirmed better, 0 confirmed worse, 0 where the runs disagree.**

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
