# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 289 | -0.9% | -9.27 to 4.02 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 292 | -0.9% | -9.12 to 3.54 | EVEN, no difference beyond the noise |
| queries a second | 4,717 | 4,672 | -0.9% | -146 to 56.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.0% | -0.253 to 0.254 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.33 | 8.33 | -0.0% | -0.375 to 0.371 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.38 | 3.41 | +0.6% | -0.0956 to 0.139 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 493 | -3.8% | -66.3 to 27.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 408 | -8.7% | -135 to 56.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 246,304 | 252,117 | +2.4% | -37,140 to 48,766 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.194 | +2.3% | -0.0123 to 0.021 | EVEN, no difference beyond the noise |
| host CPU-seconds | 105 | 107 | +2.6% | -6.9 to 12.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.34 | 2.42 | +3.4% | -0.0749 to 0.236 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 0.929 to 12.4 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 296 | +0.4% | -0.366 to 2.66 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 296 | +0.4% | -0.373 to 2.79 | EVEN, no difference beyond the noise |
| queries a second | 4,714 | 4,733 | +0.4% | -5.97 to 44.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.03 | 3.98 | -1.2% | -0.151 to 0.0553 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.37 | 5.28 | -1.8% | -0.096 to -0.096 | GAIN |
| latency, mean (ms) | 3.17 | 3.15 | -0.6% | -0.0554 to 0.015 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -36.4 to 25.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 452 | -2.1% | -18.8 to -0.636 | GAIN |
| pages read from disk into the pool (misses) | 653,146 | 655,666 | +0.4% | -62,478 to 67,519 | shown, not judged |
| host CPU busy (share of the run) | 0.189 | 0.189 | +0.2% | -0.00539 to 0.00599 | EVEN, no difference beyond the noise |
| host CPU-seconds | 312 | 313 | +0.2% | -9.84 to 11.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.32 | 2.31 | -0.2% | -0.0841 to 0.0763 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17 |  | 9.55 to 24.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 193 | +0.2% | -2.31 to 3.18 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.0% | -0.74 to 0.873 | EVEN, no difference beyond the noise |
| queries a second | 3,930 | 3,932 | +0.0% | -14.8 to 17.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.38 | 8.18 | -2.4% | -0.972 to 0.578 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.3 | 12.1 | -1.8% | -1.87 to 1.43 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.24 | 5.24 | -0.0% | -0.27 to 0.266 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 570 | +11.3% | -22 to 137 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 508 | +9.9% | -24.9 to 116 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,895 | 513,919 | -16.7% | -256,600 to 50,647 | shown, not judged |
| host CPU busy (share of the run) | 0.21 | 0.21 | -0.1% | -0.0144 to 0.0137 | EVEN, no difference beyond the noise |
| host CPU-seconds | 338 | 338 | -0.0% | -22.4 to 22.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.84 | 3.83 | -0.3% | -0.311 to 0.291 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17.3 |  | 4.83 to 29.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,945 | 2,943 | -0.1% | -12.7 to 9.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,951 | -0.0% | -10.2 to 7.64 | EVEN, no difference beyond the noise |
| queries a second | 2,952 | 2,951 | -0.0% | -10.2 to 7.64 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.336 | 0.334 | -0.6% | -0.0395 to 0.0355 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.456 | 0.451 | -1.2% | -0.0363 to 0.025 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.208 | 0.209 | +0.7% | -0.0195 to 0.0224 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 468 | -8.7% | -92.9 to 4.07 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 422 | -8.9% | -87.3 to 4.94 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,850 | 416,137 | +13.4% | -16,772 to 115,347 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.108 | +1.6% | -0.0179 to 0.0213 | EVEN, no difference beyond the noise |
| host CPU-seconds | 177 | 180 | +1.7% | -30.3 to 36.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.132 | 0.134 | +1.8% | -0.0229 to 0.0275 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12 |  | 9.52 to 14.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 273 | 322 | +17.8% | -70.5 to 168 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 990 | 988 | -0.1% | -4.7 to 1.89 | EVEN, no difference beyond the noise |
| queries a second | 990 | 988 | -0.1% | -4.7 to 1.89 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.18 | 2.8 | -12.1% | -2.2 to 1.43 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.46 | 7.05 | -16.6% | -11 to 8.19 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.16 | 1.09 | -6.3% | -0.463 to 0.318 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 396 | -22.6% | -137 to -94.8 | GAIN |
| pages holding data, mean (MB) | 453 | 329 | -27.3% | -159 to -88.2 | GAIN |
| pages read from disk into the pool (misses) | 189,622 | 275,424 | +45.2% | 73,582 to 98,022 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.113 | -2.2% | -0.0234 to 0.0184 | EVEN, no difference beyond the noise |
| host CPU-seconds | 204 | 200 | -2.1% | -41.2 to 32.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.67 | 1.37 | -18.0% | -1.21 to 0.609 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15 |  | 12.5 to 17.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
