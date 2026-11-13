# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 282 | 286 | +1.5% | -4.67 to 13.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 296 | +0.5% | -0.482 to 3.44 | EVEN, no difference beyond the noise |
| queries a second | 4,717 | 4,740 | +0.5% | -7.71 to 55.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.27 | 4.68 | -25.4% | -4.71 to 1.53 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 104 | 71.6 | -31.4% | -227 to 161 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.23 | 4.06 | -22.3% | -6.45 to 4.12 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 331 | -35.3% | -241 to -120 | GAIN |
| pages holding data, mean (MB) | 442 | 273 | -38.1% | -270 to -66.8 | GAIN |
| pages read from disk into the pool (misses) | 242,858 | 318,789 | +31.3% | 14,678 to 137,184 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.166 | +1.0% | -0.00115 to 0.00439 | EVEN, no difference beyond the noise |
| host CPU-seconds | 98.1 | 99 | +0.9% | -0.573 to 2.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.28 | 2.27 | -0.6% | -0.0556 to 0.0295 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 7 to 7 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | +0.1% | -1.82 to 2.51 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.1% | -1.76 to 2.51 | EVEN, no difference beyond the noise |
| queries a second | 4,720 | 4,726 | +0.1% | -28.2 to 40.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4 | 3.96 | -1.2% | -0.151 to 0.0553 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.54 | 5.47 | -1.2% | -0.348 to 0.217 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.12 | 3.11 | -0.3% | -0.0563 to 0.0388 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 453 | -11.4% | -199 to 81.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 409 | -11.5% | -165 to 58.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 654,477 | 799,412 | +22.1% | -366,952 to 656,823 | shown, not judged |
| host CPU busy (share of the run) | 0.184 | 0.186 | +0.8% | -0.00739 to 0.0103 | EVEN, no difference beyond the noise |
| host CPU-seconds | 305 | 308 | +1.0% | -12.6 to 18.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.26 | 2.28 | +0.8% | -0.0818 to 0.119 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 20 |  | 10.1 to 29.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 193 | -0.3% | -4.15 to 2.98 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 195 | 195 | -0.1% | -1.47 to 1.18 | EVEN, no difference beyond the noise |
| queries a second | 3,909 | 3,906 | -0.1% | -29.5 to 23.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 7.25 | 7.63 | +5.2% | -1.03 to 1.79 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.8 | 11.3 | +4.1% | -2.36 to 3.24 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.18 | 4.28 | +2.3% | -0.314 to 0.506 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 493 | -3.7% | -150 to 112 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 432 | -6.4% | -149 to 90.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 615,319 | 692,308 | +12.5% | -208,450 to 362,428 | shown, not judged |
| host CPU busy (share of the run) | 0.198 | 0.198 | +0.1% | -0.00795 to 0.00826 | EVEN, no difference beyond the noise |
| host CPU-seconds | 357 | 357 | +0.1% | -14.3 to 15 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4 | 4.02 | +0.4% | -0.183 to 0.215 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 20.3 |  | 10.9 to 29.7 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,951 | 2,948 | -0.1% | -8.82 to 2.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,950 | -0.1% | -7.84 to 3.08 | EVEN, no difference beyond the noise |
| queries a second | 2,952 | 2,950 | -0.1% | -7.84 to 3.08 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.316 | 0.316 | +0.0% | -0.0258 to 0.0258 | EVEN, the same |
| latency, 99th percentile (ms) | 0.412 | 0.409 | -0.6% | -0.0313 to 0.0267 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.193 | 0.197 | +2.3% | -0.00759 to 0.0164 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 470 | -8.2% | -195 to 111 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 427 | -7.8% | -145 to 72.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,278 | 440,630 | +20.3% | -160,595 to 309,299 | shown, not judged |
| host CPU busy (share of the run) | 0.093 | 0.0987 | +6.1% | -0.0103 to 0.0217 | EVEN, no difference beyond the noise |
| host CPU-seconds | 154 | 164 | +6.5% | -17.6 to 37.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.114 | 0.121 | +6.6% | -0.0131 to 0.0281 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.3 |  | 2.13 to 24.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 198 | 169 | -14.9% | -85.8 to 26.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 988 | +0.0% | -10.2 to 10.6 | EVEN, no difference beyond the noise |
| queries a second | 988 | 988 | +0.0% | -10.2 to 10.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.32 | 3.27 | -1.5% | -1.51 to 1.41 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.1 | 13.2 | +31.3% | -10.6 to 16.9 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.19 | 1.31 | +9.7% | -0.517 to 0.748 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 347 | -32.1% | -266 to -63.5 | GAIN |
| pages holding data, mean (MB) | 453 | 289 | -36.1% | -272 to -54.7 | GAIN |
| pages read from disk into the pool (misses) | 188,680 | 296,180 | +57.0% | 75,099 to 139,902 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.126 | +5.6% | -0.0107 to 0.024 | EVEN, no difference beyond the noise |
| host CPU-seconds | 211 | 222 | +5.6% | -18.7 to 42.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.41 | 2.92 | +20.8% | -0.18 to 1.19 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 10.9 to 18.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
