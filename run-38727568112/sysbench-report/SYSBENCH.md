# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 291 | +0.2% | -8.4 to 9.71 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 294 | +0.4% | -7.08 to 9.14 | EVEN, no difference beyond the noise |
| queries a second | 4,692 | 4,708 | +0.4% | -113 to 146 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.84 | 5.81 | -0.6% | -0.336 to 0.266 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.43 | 8.58 | +1.8% | -0.514 to 0.826 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.43 | 3.44 | +0.3% | -0.0187 to 0.0421 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 439 | -14.3% | -234 to 87.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 378 | -15.5% | -262 to 124 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 244,039 | 263,871 | +8.1% | -58,401 to 98,063 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.197 | +1.6% | -0.0039 to 0.0101 | EVEN, no difference beyond the noise |
| host CPU-seconds | 107 | 109 | +1.7% | -3.18 to 6.78 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.4 | 2.44 | +1.6% | -0.14 to 0.216 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.33 |  | 4.54 to 12.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 1.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 297 | +0.1% | -2.14 to 2.92 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.1% | -2.08 to 2.87 | EVEN, no difference beyond the noise |
| queries a second | 4,742 | 4,748 | +0.1% | -33.2 to 45.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.88 | 1.82 | -2.9% | -0.179 to 0.0694 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.53 | 3.6 | +1.8% | -0.0905 to 0.218 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.3 | 1.28 | -1.8% | -0.0801 to 0.0327 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 305 | -40.4% | -400 to -13.6 | GAIN |
| pages holding data, mean (MB) | 462 | 283 | -38.8% | -372 to 14.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 653,121 | 1,301,631 | +99.3% | 140,101 to 1,156,919 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.102 | -1.7% | -0.00542 to 0.00195 | EVEN, no difference beyond the noise |
| host CPU-seconds | 186 | 183 | -1.7% | -9.8 to 3.56 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.38 | 1.35 | -1.8% | -0.075 to 0.0261 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.33 |  | 5.46 to 11.2 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 194 | 194 | +0.2% | -0.0346 to 0.884 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 195 | 196 | +0.3% | -1.25 to 2.51 | EVEN, no difference beyond the noise |
| queries a second | 3,908 | 3,921 | +0.3% | -24.9 to 50.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.47 | 6.83 | +5.6% | -0.159 to 0.879 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.1 | 10.3 | +2.5% | -1.91 to 2.41 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.79 | 3.89 | +2.5% | -0.222 to 0.409 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 468 | -8.5% | -63.1 to -24.4 | GAIN |
| pages holding data, mean (MB) | 461 | 416 | -9.9% | -64.3 to -26.5 | GAIN |
| pages read from disk into the pool (misses) | 613,981 | 751,899 | +22.5% | 57,938 to 217,897 | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.179 | +0.3% | -0.00366 to 0.00473 | EVEN, no difference beyond the noise |
| host CPU-seconds | 321 | 322 | +0.3% | -6.5 to 8.52 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.61 | 3.61 | +0.1% | -0.0783 to 0.0852 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17 |  | 14.5 to 19.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,945 | 2,943 | -0.1% | -17.7 to 12.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,966 | 2,960 | -0.2% | -14.7 to 2.11 | EVEN, no difference beyond the noise |
| queries a second | 2,966 | 2,960 | -0.2% | -14.7 to 2.11 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.249 | 0.24 | -3.5% | -0.0311 to 0.0137 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.438 | 0.409 | -6.5% | -0.0961 to 0.0388 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.405 | 0.32 | -21.1% | -0.435 to 0.263 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 387 | -24.4% | -137 to -113 | GAIN |
| pages holding data, mean (MB) | 464 | 342 | -26.3% | -141 to -103 | GAIN |
| pages read from disk into the pool (misses) | 366,678 | 545,560 | +48.8% | 149,774 to 207,991 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.118 | +1.4% | -0.00982 to 0.013 | EVEN, no difference beyond the noise |
| host CPU-seconds | 208 | 211 | +1.3% | -17 to 22.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.155 | 0.157 | +1.5% | -0.0121 to 0.0166 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.33 |  | 2.08 to 14.6 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 38.6 | 58.2 | +50.7% | -0.974 to 40.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 985 | 986 | +0.1% | -2.97 to 5.08 | EVEN, no difference beyond the noise |
| queries a second | 985 | 986 | +0.1% | -2.97 to 5.08 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 372 | 253 | -32.0% | -321 to 83.1 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 721 | 751 | +4.1% | -1,065 to 1,124 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 85.1 | 61.1 | -28.2% | -74 to 26.1 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 435 | -15.0% | -128 to -25.7 | GAIN |
| pages holding data, mean (MB) | 454 | 356 | -21.7% | -165 to -31.9 | GAIN |
| pages read from disk into the pool (misses) | 189,504 | 257,498 | +35.9% | 33,773 to 102,214 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.131 | +0.8% | -0.0143 to 0.0164 | EVEN, no difference beyond the noise |
| host CPU-seconds | 231 | 233 | +0.6% | -25.8 to 28.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 13.4 | 9.1 | -32.3% | -5.86 to -2.84 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 21.3 |  | 19.9 to 22.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
