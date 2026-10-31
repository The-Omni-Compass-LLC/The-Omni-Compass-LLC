# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.1% | -5.45 to 4.91 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | -0.1% | -5.44 to 4.83 | EVEN, no difference beyond the noise |
| queries a second | 4,690 | 4,685 | -0.1% | -87 to 77.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.8 | 4.74 | -1.2% | -0.179 to 0.0654 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.67 | 6.51 | -2.4% | -0.496 to 0.181 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.12 | 3.13 | +0.2% | -0.0939 to 0.109 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 712 | +39.0% | 198 to 202 | power given |
| pages holding data, mean (MB) | 451 | 642 | +42.4% | 191 to 192 | power given |
| pages read from disk into the pool (misses) | 246,043 | 180,793 | -26.5% | -69,077 to -61,423 | shown, not judged |
| host CPU busy (share of the run) | 0.243 | 0.244 | +0.6% | -0.00483 to 0.00765 | EVEN, no difference beyond the noise |
| host CPU-seconds | 145 | 145 | +0.6% | -2.51 to 4.21 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.23 | 3.25 | +0.7% | -0.0603 to 0.104 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.1% | -0.89 to 0.237 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.1% | -0.804 to 0.108 | EVEN, no difference beyond the noise |
| queries a second | 4,717 | 4,711 | -0.1% | -12.9 to 1.73 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.93 | 3.84 | -2.4% | -0.194 to 0.0071 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.5 | 5.41 | -1.8% | -0.102 to -0.0937 | GAIN |
| latency, mean (ms) | 2.99 | 2.96 | -1.2% | -0.0785 to 0.00676 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 670 | +30.9% | 0.323 to 317 | power given |
| pages holding data, mean (MB) | 464 | 605 | +30.3% | -12.7 to 294 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,012 | 397,935 | -39.2% | -505,171 to -8,983 | shown, not judged |
| host CPU busy (share of the run) | 0.236 | 0.234 | -0.9% | -0.00544 to 0.00132 | EVEN, no difference beyond the noise |
| host CPU-seconds | 420 | 416 | -0.9% | -9.71 to 2.29 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.12 | 3.09 | -0.8% | -0.0735 to 0.0263 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 196 | +2.1% | 2.46 to 5.53 | GAIN |
| throughput (transactions a second) | 197 | 197 | +0.1% | -2.46 to 2.97 | EVEN, no difference beyond the noise |
| queries a second | 3,936 | 3,942 | +0.1% | -49.2 to 59.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.48 | 6.59 | -22.3% | -2.5 to -1.28 | GAIN |
| latency, 99th percentile (ms) | 12.8 | 8.58 | -33.1% | -5.26 to -3.24 | GAIN |
| latency, mean (ms) | 5.14 | 4.77 | -7.2% | -0.636 to -0.102 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,036 | +102.3% | 512 to 536 | power given |
| pages holding data, mean (MB) | 463 | 927 | +100.3% | 440 to 489 | power given |
| pages read from disk into the pool (misses) | 618,403 | 126,614 | -79.5% | -529,254 to -454,324 | shown, not judged |
| host CPU busy (share of the run) | 0.277 | 0.257 | -7.2% | -0.0248 to -0.0149 | GAIN |
| host CPU-seconds | 486 | 451 | -7.2% | -43.7 to -26.5 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.52 | 5.02 | -9.1% | -0.582 to -0.423 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,948 | 2,956 | +0.3% | -1.11 to 16.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,964 | 2,967 | +0.1% | -4.24 to 10.9 | EVEN, no difference beyond the noise |
| queries a second | 2,964 | 2,967 | +0.1% | -4.24 to 10.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.232 | 0.221 | -4.7% | -0.0239 to 0.00191 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.382 | 0.367 | -3.8% | -0.084 to 0.0553 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.46 | 0.296 | -35.6% | -0.842 to 0.515 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,224 | +139.0% | 565 to 858 | power given |
| pages holding data, mean (MB) | 465 | 924 | +98.7% | 438 to 480 | power given |
| pages read from disk into the pool (misses) | 368,437 | 76,298 | -79.3% | -298,059 to -286,219 | shown, not judged |
| host CPU busy (share of the run) | 0.115 | 0.114 | -0.2% | -0.0011 to 0.000624 | EVEN, no difference beyond the noise |
| host CPU-seconds | 204 | 203 | -0.2% | -2.14 to 1.17 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.152 | 0.151 | -0.5% | -0.00199 to 0.0005 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9.33 |  | -2.92 to 21.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 3.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 28.8 | 33.8 | +17.2% | -5.22 to 15.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 984 | +0.1% | -5.79 to 7.27 | EVEN, no difference beyond the noise |
| queries a second | 983 | 984 | +0.1% | -5.79 to 7.27 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.46 | 1.39 | -4.4% | -0.35 to 0.221 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.21 | 1.91 | -13.5% | -1.52 to 0.923 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.13 | 0.921 | -18.6% | -1.13 to 0.706 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,235 | +141.3% | 702 to 745 | power given |
| pages holding data, mean (MB) | 457 | 888 | +94.4% | 406 to 456 | power given |
| pages read from disk into the pool (misses) | 190,205 | 71,594 | -62.4% | -129,609 to -107,613 | shown, not judged |
| host CPU busy (share of the run) | 0.221 | 0.215 | -2.7% | -0.0325 to 0.0205 | EVEN, no difference beyond the noise |
| host CPU-seconds | 388 | 378 | -2.7% | -56.5 to 35.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 30.9 | 24.6 | -20.3% | -25.3 to 12.8 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
