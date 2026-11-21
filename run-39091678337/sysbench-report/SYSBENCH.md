# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 296 | +0.0% | -0.769 to 1.02 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.1% | -0.956 to 1.79 | EVEN, no difference beyond the noise |
| queries a second | 4,738 | 4,744 | +0.1% | -15.3 to 28.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.83 | 2.78 | -1.8% | -0.296 to 0.196 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.31 | 4.36 | +1.2% | -0.69 to 0.794 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.39 | +3.6% | -0.134 to 0.232 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 348 | -32.0% | -391 to 62.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 442 | 291 | -34.1% | -303 to 0.945 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 241,374 | 314,335 | +30.2% | -17,680 to 163,601 | shown, not judged |
| host CPU busy (share of the run) | 0.1 | 0.103 | +3.0% | -0.0113 to 0.0173 | EVEN, no difference beyond the noise |
| host CPU-seconds | 60.1 | 62 | +3.1% | -6.9 to 10.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.34 | 1.37 | +2.9% | -0.148 to 0.226 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | -3.61 to 13.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 297 | +0.3% | -3.05 to 4.75 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.3% | -3.28 to 4.83 | EVEN, no difference beyond the noise |
| queries a second | 4,738 | 4,750 | +0.3% | -52.4 to 77.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.73 | 1.68 | -3.0% | -0.285 to 0.183 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.19 | 3.1 | -2.9% | -0.679 to 0.492 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.22 | 1.22 | -0.2% | -0.166 to 0.162 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 363 | -29.0% | -316 to 19.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 331 | -28.2% | -282 to 21.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 653,743 | 1,077,694 | +64.8% | -125,703 to 973,605 | shown, not judged |
| host CPU busy (share of the run) | 0.0966 | 0.0962 | -0.5% | -0.0133 to 0.0124 | EVEN, no difference beyond the noise |
| host CPU-seconds | 174 | 173 | -0.5% | -23.9 to 22.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.29 | 1.28 | -0.7% | -0.186 to 0.167 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 5.16 to 15.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 193 | +0.3% | -0.611 to 1.76 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.3% | -1.55 to 2.75 | EVEN, no difference beyond the noise |
| queries a second | 3,935 | 3,947 | +0.3% | -31.1 to 55 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.53 | 8.43 | -1.2% | -0.881 to 0.685 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.7 | 12.7 | +0.1% | -1.12 to 1.14 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.27 | 5.25 | -0.4% | -0.217 to 0.175 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 549 | +7.3% | -53.3 to 128 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 489 | +5.8% | -47.6 to 101 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 618,717 | 545,386 | -11.9% | -234,061 to 87,397 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.207 | -1.1% | -0.011 to 0.00637 | EVEN, no difference beyond the noise |
| host CPU-seconds | 336 | 332 | -1.1% | -17.4 to 10.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.81 | 3.76 | -1.4% | -0.201 to 0.0966 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19 |  | 14 to 24 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,924 | 2,925 | +0.0% | -6.63 to 7.95 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,933 | 2,934 | +0.0% | -9.39 to 9.91 | EVEN, no difference beyond the noise |
| queries a second | 2,933 | 2,934 | +0.0% | -9.39 to 9.91 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.253 | 0.231 | -8.7% | -0.0525 to 0.00853 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.459 | 0.451 | -1.7% | -0.008 to -0.008 | GAIN |
| latency, mean (ms) | 0.185 | 0.146 | -21.2% | -0.184 to 0.106 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 441 | -13.8% | -142 to 1.14 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 404 | -12.8% | -123 to 4.38 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,250 | 447,736 | +21.9% | -17,058 to 178,030 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.111 | -0.9% | -0.00491 to 0.00287 | EVEN, no difference beyond the noise |
| host CPU-seconds | 203 | 201 | -0.9% | -9.3 to 5.46 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.151 | 0.15 | -1.0% | -0.00693 to 0.00404 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11.3 |  | 5.08 to 17.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 4.96 | 5.38 | +8.4% | -6.41 to 7.24 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 983 | -0.1% | -5.96 to 3.88 | EVEN, no difference beyond the noise |
| queries a second | 984 | 983 | -0.1% | -5.96 to 3.88 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.75 | 1.72 | -1.4% | -0.226 to 0.177 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.37 | 3.43 | +1.7% | -0.34 to 0.455 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.07 | 1.07 | -0.2% | -0.102 to 0.0991 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 515 | +0.6% | -15.9 to 21.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 447 | -1.4% | -14.2 to 1.31 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 188,589 | 189,422 | +0.4% | -18,328 to 19,994 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.121 | -4.3% | -0.033 to 0.0222 | EVEN, no difference beyond the noise |
| host CPU-seconds | 194 | 186 | -4.2% | -49.8 to 33.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 142 | 81.4 | -42.6% | -284 to 164 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.3 |  | 3.29 to 23.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
