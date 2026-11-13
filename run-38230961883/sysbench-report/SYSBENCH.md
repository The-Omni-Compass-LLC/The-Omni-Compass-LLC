# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 289 | 291 | +0.5% | -4.84 to 8.01 | no difference beyond the noise |
| throughput (transactions a second) | 291 | 293 | +0.7% | -3.26 to 7.14 | no difference beyond the noise |
| queries a second | 4,654 | 4,685 | +0.7% | -52.2 to 114 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.77 | 5.91 | +2.4% | -0.0128 to 0.294 | no difference beyond the noise |
| latency, 99th percentile (ms) | 7.61 | 7.85 | +3.1% | -0.509 to 0.983 | no difference beyond the noise |
| latency, mean (ms) | 3.45 | 3.51 | +2.0% | -0.032 to 0.167 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -36.5 to 23.7 | no difference beyond the noise |
| pages holding data, mean (MB) | 444 | 436 | -1.9% | -43.6 to 26.9 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 169,724 | 171,354 | +1.0% | -15,133 to 18,393 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.207 | +3.7% | 0.00669 to 0.00792 | **WORSE** |
| host CPU-seconds | 74.1 | 77 | +3.9% | 2.54 to 3.25 | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 2.48 | 2.56 | +3.3% | 0.0292 to 0.132 | **WORSE** |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.1% | -5.23 to 5.68 | no difference beyond the noise |
| throughput (transactions a second) | 292 | 292 | +0.1% | -5.37 to 5.71 | no difference beyond the noise |
| queries a second | 4,675 | 4,678 | +0.1% | -85.9 to 91.4 | no difference beyond the noise |
| latency, 95th percentile (ms) | 4.35 | 4.35 | +0.0% | -0.194 to 0.194 | same |
| latency, 99th percentile (ms) | 6.02 | 5.84 | -3.0% | -0.332 to -0.0248 | better |
| latency, mean (ms) | 3.24 | 3.24 | +0.1% | -0.0745 to 0.078 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 487 | -4.9% | -112 to 62.4 | no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 430 | -6.7% | -111 to 48.8 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 455,050 | 498,606 | +9.6% | -94,663 to 181,776 | shown, not judged |
| host CPU busy (share of the run) | 0.198 | 0.201 | +1.6% | -0.000779 to 0.00719 | no difference beyond the noise |
| host CPU-seconds | 220 | 224 | +1.8% | -1.25 to 9.18 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.45 | 2.49 | +1.7% | -0.0622 to 0.147 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 5.03 to 15 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 191 | +0.2% | -1.27 to 2.02 | no difference beyond the noise |
| throughput (transactions a second) | 195 | 195 | -0.2% | -0.94 to 0.00825 | no difference beyond the noise |
| queries a second | 3,900 | 3,891 | -0.2% | -18.8 to 0.165 | no difference beyond the noise |
| latency, 95th percentile (ms) | 8.84 | 8.43 | -4.6% | -1.19 to 0.373 | no difference beyond the noise |
| latency, 99th percentile (ms) | 12.8 | 12.4 | -3.5% | -1.55 to 0.655 | no difference beyond the noise |
| latency, mean (ms) | 5.48 | 5.41 | -1.4% | -0.0972 to -0.0589 | better |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 594 | +16.1% | -109 to 273 | no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 523 | +13.5% | -72 to 196 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 434,290 | 345,775 | -20.4% | -267,192 to 90,162 | shown, not judged |
| host CPU busy (share of the run) | 0.23 | 0.224 | -2.7% | -0.0106 to -0.00197 | better |
| host CPU-seconds | 250 | 243 | -2.7% | -11.2 to -2.19 | better |
| host CPU-seconds per 1,000 transactions inside the line | 4.26 | 4.14 | -2.9% | -0.167 to -0.0765 | better |
| buffer pool size changes written (the knob's moves) | 0 | 15 |  | 10.7 to 19.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,925 | 2,925 | -0.0% | -8.31 to 7.58 | no difference beyond the noise |
| throughput (transactions a second) | 2,933 | 2,933 | -0.0% | -10.8 to 9.28 | no difference beyond the noise |
| queries a second | 2,933 | 2,933 | -0.0% | -10.8 to 9.28 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.379 | 0.365 | -3.5% | -0.032 to 0.00531 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.485 | 0.47 | -3.1% | -0.0615 to 0.0315 | no difference beyond the noise |
| latency, mean (ms) | 0.212 | 0.205 | -3.3% | -0.0219 to 0.00781 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 481 | -6.0% | -115 to 53.6 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 434 | -6.1% | -73.1 to 17.2 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 262,315 | 282,414 | +7.7% | -66,169 to 106,367 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.105 | -5.5% | -0.0204 to 0.00805 | no difference beyond the noise |
| host CPU-seconds | 124 | 117 | -5.6% | -22.8 to 9.03 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.138 | 0.13 | -5.5% | -0.0253 to 0.00998 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9.33 |  | 3.6 to 15.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1.78 | 1.43 | -19.8% | -2.69 to 1.99 | no difference beyond the noise |
| throughput (transactions a second) | 969 | 969 | -0.0% | -7.61 to 7.55 | no difference beyond the noise |
| queries a second | 969 | 969 | -0.0% | -7.61 to 7.55 | no difference beyond the noise |
| latency, 95th percentile (ms) | 1.78 | 1.78 | +0.3% | -0.307 to 0.316 | no difference beyond the noise |
| latency, 99th percentile (ms) | 18.4 | 4.29 | -76.7% | -77.4 to 49.1 | no difference beyond the noise |
| latency, mean (ms) | 1.95 | 1.64 | -15.6% | -1.9 to 1.29 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 369 | -28.0% | -185 to -102 | better |
| pages holding data, mean (MB) | 448 | 307 | -31.5% | -202 to -80.8 | better |
| pages read from disk into the pool (misses) | 139,971 | 200,804 | +43.5% | 42,893 to 78,773 | shown, not judged |
| host CPU busy (share of the run) | 0.177 | 0.178 | +0.9% | -0.0211 to 0.0244 | no difference beyond the noise |
| host CPU-seconds | 212 | 214 | +0.9% | -25 to 29 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 436 | 533 | +22.3% | -604 to 798 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12 |  | 7.7 to 16.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
