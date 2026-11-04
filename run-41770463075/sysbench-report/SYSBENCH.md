# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 294 | +0.5% | -4.19 to 7.07 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.4% | -4.77 to 7.2 | STEADY, no difference beyond the noise |
| queries a second | 4,704 | 4,724 | +0.4% | -76.3 to 115 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.94 | 4.94 | +0.0% | 0 to 0 | STEADY, the same |
| latency, 99th percentile (ms) | 7.08 | 6.83 | -3.5% | -0.265 to -0.236 | GAIN |
| latency, mean (ms) | 3.21 | 3.18 | -0.9% | -0.169 to 0.114 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 712 | +39.1% | -50.1 to 450 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 641 | +41.2% | -32.7 to 406 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 247,320 | 180,786 | -26.9% | -140,147 to 7,080 | shown, not judged |
| host CPU busy (share of the run) | 0.249 | 0.249 | -0.2% | -0.0173 to 0.0165 | STEADY, no difference beyond the noise |
| host CPU-seconds | 148 | 148 | -0.2% | -10.2 to 9.75 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.3 | 3.28 | -0.7% | -0.18 to 0.136 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | +0.2% | -2.15 to 3.08 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.1% | -2.13 to 2.87 | STEADY, no difference beyond the noise |
| queries a second | 4,718 | 4,724 | +0.1% | -34.1 to 45.9 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.16 | 3.98 | -4.4% | -1.3 to 0.931 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.55 | 5.31 | -4.4% | -1.71 to 1.22 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.11 | 3.03 | -2.7% | -0.546 to 0.378 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 605 | +18.2% | -309 to 496 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 544 | +17.6% | -261 to 424 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,608 | 519,898 | -20.7% | -709,534 to 438,114 | shown, not judged |
| host CPU busy (share of the run) | 0.246 | 0.241 | -2.3% | -0.0385 to 0.0271 | STEADY, no difference beyond the noise |
| host CPU-seconds | 438 | 428 | -2.3% | -67.5 to 47.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.25 | 3.17 | -2.4% | -0.512 to 0.355 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.667 |  | -2.2 to 3.54 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 197 | +2.2% | 1.36 to 7.24 | GAIN |
| throughput (transactions a second) | 197 | 197 | +0.1% | -2.35 to 2.6 | STEADY, no difference beyond the noise |
| queries a second | 3,937 | 3,939 | +0.1% | -47.1 to 52 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.58 | 6.87 | -19.9% | -1.82 to -1.59 | GAIN |
| latency, 99th percentile (ms) | 12.8 | 8.79 | -31.5% | -4.32 to -3.76 | GAIN |
| latency, mean (ms) | 5.21 | 4.86 | -6.7% | -0.471 to -0.227 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,040 | +103.2% | 513 to 544 | power given |
| pages holding data, mean (MB) | 463 | 930 | +101.1% | 443 to 492 | power given |
| pages read from disk into the pool (misses) | 616,632 | 119,616 | -80.6% | -560,422 to -433,610 | shown, not judged |
| host CPU busy (share of the run) | 0.279 | 0.261 | -6.4% | -0.0307 to -0.00519 | GAIN |
| host CPU-seconds | 491 | 459 | -6.5% | -53.7 to -10.2 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.58 | 5.1 | -8.5% | -0.643 to -0.31 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,937 | 2,937 | -0.0% | -27 to 26.7 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,954 | +0.1% | -2.07 to 5.96 | STEADY, no difference beyond the noise |
| queries a second | 2,952 | 2,954 | +0.1% | -2.07 to 5.96 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.342 | 0.357 | +4.2% | -0.0574 to 0.0861 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.54 | 0.55 | +1.9% | -0.112 to 0.132 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.205 | 0.217 | +5.7% | -0.0216 to 0.0449 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 540 | +5.5% | -93.5 to 150 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 487 | +5.0% | -99 to 145 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,698 | 342,176 | -6.9% | -123,223 to 72,179 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.173 | +5.8% | -0.0129 to 0.032 | STEADY, no difference beyond the noise |
| host CPU-seconds | 288 | 305 | +5.9% | -21.7 to 55.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.214 | 0.227 | +5.9% | -0.018 to 0.0434 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 32.7 | 44.9 | +37.1% | -11.5 to 35.8 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 984 | 984 | -0.0% | -6.94 to 6.14 | STEADY, no difference beyond the noise |
| queries a second | 984 | 984 | -0.0% | -6.94 to 6.14 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.46 | 1.38 | -5.9% | -0.321 to 0.147 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.38 | 2.17 | -8.5% | -0.602 to 0.198 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.938 | 0.906 | -3.4% | -0.131 to 0.068 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.3% | 700 to 747 | power given |
| pages holding data, mean (MB) | 456 | 888 | +94.5% | 404 to 458 | power given |
| pages read from disk into the pool (misses) | 192,406 | 71,780 | -62.7% | -128,650 to -112,602 | shown, not judged |
| host CPU busy (share of the run) | 0.223 | 0.213 | -4.5% | -0.0376 to 0.0175 | STEADY, no difference beyond the noise |
| host CPU-seconds | 392 | 374 | -4.5% | -65.5 to 30.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 26.7 | 18.4 | -31.4% | -26 to 9.22 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
