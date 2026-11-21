# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 294 | +0.3% | -8.78 to 10.6 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.1% | -9.42 to 10 | EVEN, no difference beyond the noise |
| queries a second | 4,712 | 4,717 | +0.1% | -151 to 160 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.1 | 3.02 | -2.7% | -1.05 to 0.88 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.61 | 4.6 | -18.0% | -5.89 to 3.88 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.49 | 1.45 | -2.8% | -0.454 to 0.37 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 398 | -22.3% | -178 to -50.4 | GAIN |
| pages holding data, mean (MB) | 444 | 338 | -23.9% | -168 to -43.4 | GAIN |
| pages read from disk into the pool (misses) | 244,780 | 281,426 | +15.0% | 10,729 to 62,563 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.106 | +0.6% | -0.0134 to 0.0148 | EVEN, no difference beyond the noise |
| host CPU-seconds | 63.3 | 63.6 | +0.5% | -8.03 to 8.69 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.42 | 1.42 | +0.3% | -0.2 to 0.209 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 |  | 0.162 to 10.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.1% | -4.09 to 4.48 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 292 | +0.1% | -4.23 to 4.62 | EVEN, no difference beyond the noise |
| queries a second | 4,676 | 4,679 | +0.1% | -67.7 to 73.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.74 | 2.63 | -4.1% | -0.294 to 0.069 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.41 | 4.15 | -5.8% | -0.551 to 0.038 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.07 | 2.01 | -3.2% | -0.235 to 0.103 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 412 | -19.5% | -251 to 51.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 375 | -18.8% | -206 to 33.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,056 | 908,265 | +38.7% | -143,687 to 650,105 | shown, not judged |
| host CPU busy (share of the run) | 0.159 | 0.157 | -1.7% | -0.00975 to 0.00446 | EVEN, no difference beyond the noise |
| host CPU-seconds | 292 | 287 | -1.7% | -17.8 to 8.02 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.16 | 2.13 | -1.7% | -0.164 to 0.0893 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 8.93 to 20.4 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 192 | -0.3% | -2.26 to 1.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.5% | -3.3 to 1.43 | EVEN, no difference beyond the noise |
| queries a second | 3,937 | 3,918 | -0.5% | -66.1 to 28.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.54 | 8.33 | -2.4% | -0.798 to 0.39 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.5 | 12.5 | -0.6% | -0.721 to 0.575 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.41 | 5.36 | -0.9% | -0.299 to 0.198 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 541 | +5.6% | -41.2 to 98.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 487 | +5.3% | -30.7 to 79.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,489 | 554,077 | -10.1% | -264,581 to 139,756 | shown, not judged |
| host CPU busy (share of the run) | 0.221 | 0.217 | -1.9% | -0.0209 to 0.0123 | EVEN, no difference beyond the noise |
| host CPU-seconds | 356 | 350 | -1.8% | -33.5 to 20.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.04 | 3.98 | -1.6% | -0.333 to 0.207 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 10.9 to 18.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,943 | 2,947 | +0.1% | -2.15 to 10.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,951 | 2,954 | +0.1% | -3.39 to 10.8 | EVEN, no difference beyond the noise |
| queries a second | 2,951 | 2,954 | +0.1% | -3.39 to 10.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.318 | 0.314 | -1.3% | -0.0268 to 0.0188 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.462 | 0.451 | -2.4% | -0.0218 to -0.000171 | GAIN |
| latency, mean (ms) | 0.198 | 0.198 | +0.3% | -3.13e-05 to 0.00123 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 489 | -4.5% | -75.8 to 29.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 440 | -5.1% | -62.9 to 15.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 364,912 | 381,592 | +4.6% | -64,810 to 98,169 | shown, not judged |
| host CPU busy (share of the run) | 0.0946 | 0.0971 | +2.7% | -0.00315 to 0.00831 | EVEN, no difference beyond the noise |
| host CPU-seconds | 156 | 161 | +2.9% | -5.39 to 14.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.116 | 0.12 | +2.8% | -0.00405 to 0.0105 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 8.41 to 20.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0.0943 | 0.0986 | +4.6% | -0.0983 to 0.107 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 979 | 979 | -0.1% | -5.64 to 4.57 | EVEN, no difference beyond the noise |
| queries a second | 979 | 979 | -0.1% | -5.64 to 4.57 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.88 | 1.82 | -2.7% | -0.405 to 0.304 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.96 | 3.84 | -3.2% | -0.757 to 0.507 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.29 | 1.26 | -2.4% | -0.358 to 0.296 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 420 | -17.9% | -152 to -30.6 | GAIN |
| pages holding data, mean (MB) | 452 | 357 | -21.1% | -141 to -50.1 | GAIN |
| pages read from disk into the pool (misses) | 189,422 | 256,314 | +35.3% | 12,058 to 121,727 | shown, not judged |
| host CPU busy (share of the run) | 0.17 | 0.17 | -0.4% | -0.0262 to 0.0248 | EVEN, no difference beyond the noise |
| host CPU-seconds | 304 | 302 | -0.4% | -46.9 to 44.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 7,388 | 8,955 | +21.2% | -11,818 to 14,952 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17.3 |  | 6.99 to 27.7 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
