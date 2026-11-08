# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | +0.1% | -3.5 to 3.81 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.2% | -3.47 to 4.75 | STEADY, no difference beyond the noise |
| queries a second | 4,716 | 4,727 | +0.2% | -55.5 to 76 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.67 | 3.01 | +12.9% | -0.938 to 1.62 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.13 | 4.73 | +14.4% | -1.55 to 2.74 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.37 | 1.51 | +10.5% | -0.427 to 0.714 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 771 | +502.6% | 171 to 1,116 | power given |
| pages holding data, mean (MB) | 121 | 643 | +432.4% | 253 to 791 | power given |
| pages read from disk into the pool (misses) | 593,260 | 237,562 | -60.0% | -410,562 to -300,833 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.106 | +2.6% | -0.0127 to 0.0182 | STEADY, no difference beyond the noise |
| host CPU-seconds | 62.1 | 63.7 | +2.6% | -7.53 to 10.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.39 | 1.42 | +2.5% | -0.158 to 0.226 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | +0.0% | -5.67 to 5.78 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.1% | -5.24 to 5.8 | STEADY, no difference beyond the noise |
| queries a second | 4,701 | 4,705 | +0.1% | -83.8 to 92.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.04 | 3.21 | +5.6% | -0.212 to 0.551 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.1 | 4.41 | +7.6% | -0.217 to 0.837 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.37 | 2.41 | +1.6% | -0.0701 to 0.146 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 494 | +286.0% | 329 to 404 | power given |
| pages holding data, mean (MB) | 120 | 454 | +278.5% | 320 to 349 | power given |
| pages read from disk into the pool (misses) | 1,981,006 | 685,864 | -65.4% | -1,491,150 to -1,099,136 | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.198 | +1.0% | -0.0083 to 0.0121 | STEADY, no difference beyond the noise |
| host CPU-seconds | 357 | 361 | +1.0% | -15.1 to 22.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.65 | 2.67 | +0.9% | -0.0931 to 0.142 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 2.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 181 | 196 | +8.6% | 14.4 to 16.5 | GAIN |
| throughput (transactions a second) | 196 | 197 | +0.3% | 0.633 to 0.637 | GAIN |
| queries a second | 3,921 | 3,934 | +0.3% | 12.7 to 12.7 | GAIN |
| latency, 95th percentile (ms) | 12.3 | 6.96 | -43.4% | -5.71 to -4.97 | GAIN |
| latency, 99th percentile (ms) | 17.4 | 9.01 | -48.3% | -10.8 to -6 | GAIN |
| latency, mean (ms) | 6.3 | 4.96 | -21.4% | -2.54 to -0.152 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,054 | +723.7% | 796 to 1,057 | power given |
| pages holding data, mean (MB) | 118 | 942 | +695.3% | 711 to 936 | power given |
| pages read from disk into the pool (misses) | 1,663,345 | 131,214 | -92.1% | -1,719,309 to -1,344,953 | shown, not judged |
| host CPU busy (share of the run) | 0.313 | 0.267 | -14.8% | -0.0579 to -0.0348 | GAIN |
| host CPU-seconds | 551 | 469 | -14.9% | -103 to -61 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 6.66 | 5.22 | -21.6% | -1.67 to -1.21 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 5.23 to 8.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,929 | 2,933 | +0.2% | -7.78 to 17.3 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,936 | 2,935 | -0.0% | -20.3 to 18.7 | STEADY, no difference beyond the noise |
| queries a second | 2,936 | 2,935 | -0.0% | -20.3 to 18.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.214 | 0.206 | -3.7% | -0.032 to 0.016 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.43 | 0.419 | -2.4% | -0.0513 to 0.0307 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.156 | 0.124 | -20.2% | -0.0977 to 0.0348 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 366 | +186.1% | 238 to 238 | power given |
| pages holding data, mean (MB) | 121 | 348 | +187.1% | 227 to 227 | power given |
| pages read from disk into the pool (misses) | 1,029,833 | 550,328 | -46.6% | -483,285 to -475,725 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.11 | -4.4% | -0.0142 to 0.00398 | STEADY, no difference beyond the noise |
| host CPU-seconds | 210 | 201 | -4.5% | -25.6 to 6.76 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.156 | 0.149 | -4.6% | -0.0188 to 0.00435 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 178 | 241 | +35.6% | -47.1 to 173 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 987 | 988 | +0.1% | -0.664 to 2.79 | STEADY, no difference beyond the noise |
| queries a second | 987 | 988 | +0.1% | -0.664 to 2.79 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.31 | 4.35 | +31.5% | -3.84 to 5.92 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 14.9 | 13.1 | -11.7% | -18.1 to 14.6 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.41 | 1.75 | +23.7% | -0.7 to 1.37 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,301 | +916.4% | 1,169 to 1,177 | power given |
| pages holding data, mean (MB) | 118 | 881 | +646.2% | 756 to 770 | power given |
| pages read from disk into the pool (misses) | 415,318 | 70,880 | -82.9% | -358,443 to -330,433 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.114 | -17.4% | -0.0494 to 0.00138 | STEADY, no difference beyond the noise |
| host CPU-seconds | 242 | 200 | -17.4% | -86.4 to 2.09 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.14 | 1.84 | -41.4% | -3.71 to 1.11 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
