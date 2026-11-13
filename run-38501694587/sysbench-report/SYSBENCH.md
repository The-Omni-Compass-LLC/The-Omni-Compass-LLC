# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 293 | -0.2% | -7.73 to 6.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.0% | -7.08 to 7.03 | EVEN, no difference beyond the noise |
| queries a second | 4,720 | 4,720 | -0.0% | -113 to 112 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.37 | 5.37 | -0.0% | -0.422 to 0.419 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.48 | 7.75 | +3.7% | -0.414 to 0.965 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.36 | 3.39 | +0.8% | -0.00443 to 0.0556 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 445 | -13.1% | -140 to 6.09 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 381 | -14.8% | -155 to 22.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 244,982 | 257,953 | +5.3% | -42,054 to 67,995 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.2 | +2.4% | 0.00183 to 0.00736 | power given |
| host CPU-seconds | 108 | 111 | +2.7% | 1.19 to 4.67 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 2.39 | 2.46 | +2.8% | 0.0105 to 0.123 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 5.16 to 15.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | +0.0% | -2.75 to 2.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | -0.0% | -2.87 to 2.66 | EVEN, no difference beyond the noise |
| queries a second | 4,694 | 4,693 | -0.0% | -45.9 to 42.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.16 | 2.98 | -5.4% | -0.917 to 0.575 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.07 | 4.82 | -4.8% | -1.32 to 0.826 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.2 | 2.14 | -2.9% | -0.291 to 0.161 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 400 | -22.0% | -250 to 24.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 367 | -20.4% | -219 to 31.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 656,152 | 986,080 | +50.3% | -148,690 to 808,547 | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.172 | -1.8% | -0.0166 to 0.0104 | EVEN, no difference beyond the noise |
| host CPU-seconds | 318 | 312 | -1.7% | -29.6 to 18.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.35 | 2.31 | -1.7% | -0.206 to 0.124 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15 |  | 12.5 to 17.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195 | 194 | -0.2% | -1.36 to 0.627 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 195 | -0.2% | -0.952 to 0.11 | EVEN, no difference beyond the noise |
| queries a second | 3,915 | 3,906 | -0.2% | -19 to 2.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.6 | 6.71 | +1.7% | -0.766 to 0.984 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 9.46 | 9.39 | -0.7% | -1.14 to 0.997 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.31 | 4.38 | +1.8% | -0.15 to 0.303 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 466 | -9.1% | -64 to -29 | GAIN |
| pages holding data, mean (MB) | 462 | 419 | -9.3% | -49.7 to -36 | GAIN |
| pages read from disk into the pool (misses) | 614,306 | 747,663 | +21.7% | 42,284 to 224,429 | shown, not judged |
| host CPU busy (share of the run) | 0.228 | 0.226 | -1.1% | -0.0201 to 0.0149 | EVEN, no difference beyond the noise |
| host CPU-seconds | 410 | 405 | -1.1% | -35.3 to 26.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.57 | 4.53 | -0.9% | -0.405 to 0.325 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18 |  | 9.04 to 27 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,947 | 2,946 | -0.0% | -6.27 to 3.33 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,954 | 2,953 | -0.0% | -6.34 to 3.65 | EVEN, no difference beyond the noise |
| queries a second | 2,954 | 2,953 | -0.0% | -6.34 to 3.65 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.34 | 0.338 | -0.6% | -0.0248 to 0.0208 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.47 | 0.461 | -1.8% | -0.0298 to 0.0125 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.206 | 0.208 | +1.1% | -0.000806 to 0.00538 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 446 | -12.8% | -176 to 45 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 398 | -14.2% | -162 to 29.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,197 | 476,058 | +29.6% | -74,899 to 292,621 | shown, not judged |
| host CPU busy (share of the run) | 0.106 | 0.108 | +2.6% | 0.000289 to 0.00513 | power given |
| host CPU-seconds | 175 | 180 | +2.8% | 0.689 to 8.99 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.13 | 0.134 | +2.8% | 0.000353 to 0.00696 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 13.7 |  | 12.2 to 15.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 249 | 296 | +18.9% | -104 to 198 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 987 | -0.1% | -3.79 to 1.71 | EVEN, no difference beyond the noise |
| queries a second | 988 | 987 | -0.1% | -3.79 to 1.71 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.54 | 2.28 | -10.2% | -0.828 to 0.311 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.97 | 4.71 | -5.3% | -0.47 to -0.0537 | GAIN |
| latency, mean (ms) | 0.955 | 0.956 | +0.2% | -0.233 to 0.236 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 285 | -44.4% | -314 to -141 | GAIN |
| pages holding data, mean (MB) | 453 | 244 | -46.1% | -305 to -113 | GAIN |
| pages read from disk into the pool (misses) | 189,130 | 322,653 | +70.6% | 103,639 to 163,408 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.116 | -0.2% | -0.0244 to 0.024 | EVEN, no difference beyond the noise |
| host CPU-seconds | 204 | 204 | -0.2% | -42.5 to 41.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.87 | 1.52 | -18.7% | -1.93 to 1.23 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 7 to 7 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
