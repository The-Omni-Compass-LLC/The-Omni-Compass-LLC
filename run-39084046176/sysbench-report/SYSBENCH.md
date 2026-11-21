# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.2% | -9.24 to 7.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.2% | -9.28 to 8.12 | EVEN, no difference beyond the noise |
| queries a second | 4,725 | 4,716 | -0.2% | -149 to 130 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3 | 2.9 | -3.6% | -0.338 to 0.124 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.66 | 4.6 | -1.2% | -0.702 to 0.587 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.41 | 1.41 | +0.1% | -0.0736 to 0.0778 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 354 | -30.9% | -319 to 2.89 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 442 | 305 | -31.0% | -300 to 26.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,364 | 298,440 | +21.6% | -26,469 to 132,621 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.103 | +0.1% | -0.00413 to 0.00434 | EVEN, no difference beyond the noise |
| host CPU-seconds | 61.8 | 61.9 | +0.2% | -2.45 to 2.64 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.38 | 1.38 | +0.4% | -0.0705 to 0.0809 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 |  | 0.538 to 8.13 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 296 | +0.0% | -3.44 to 3.65 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | +0.0% | -3.54 to 3.78 | EVEN, no difference beyond the noise |
| queries a second | 4,741 | 4,743 | +0.0% | -56.7 to 60.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.78 | 1.76 | -1.2% | -0.117 to 0.0727 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.25 | 3.13 | -3.6% | -0.493 to 0.259 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.24 | 1.25 | +0.5% | -0.0519 to 0.0646 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 330 | -35.6% | -277 to -88.1 | GAIN |
| pages holding data, mean (MB) | 462 | 297 | -35.7% | -243 to -86.5 | GAIN |
| pages read from disk into the pool (misses) | 655,100 | 1,180,080 | +80.1% | 119,379 to 930,582 | shown, not judged |
| host CPU busy (share of the run) | 0.0987 | 0.0994 | +0.7% | -0.00273 to 0.00406 | EVEN, no difference beyond the noise |
| host CPU-seconds | 177 | 179 | +0.7% | -4.85 to 7.28 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.31 | 1.32 | +0.7% | -0.0503 to 0.0674 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 2.41 to 14.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 192 | -0.3% | -2.05 to 0.717 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.0% | -1.81 to 1.62 | EVEN, no difference beyond the noise |
| queries a second | 3,928 | 3,926 | -0.0% | -36.2 to 32.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.18 | 8.43 | +3.0% | 0.0439 to 0.451 | LOSS |
| latency, 99th percentile (ms) | 12.1 | 12.4 | +3.0% | 0.057 to 0.677 | LOSS |
| latency, mean (ms) | 5.16 | 5.21 | +1.0% | -0.16 to 0.261 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 506 | -1.1% | -40.1 to 29 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 458 | -1.0% | -33.2 to 24.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 617,045 | 621,648 | +0.7% | -58,543 to 67,747 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.208 | +0.9% | -0.0161 to 0.0198 | EVEN, no difference beyond the noise |
| host CPU-seconds | 332 | 335 | +1.0% | -26.3 to 33 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.76 | 3.81 | +1.4% | -0.305 to 0.407 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.7 |  | 10.7 to 26.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,951 | 2,949 | -0.1% | -11.5 to 7.79 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,956 | 2,955 | -0.0% | -9.88 to 7.22 | EVEN, no difference beyond the noise |
| queries a second | 2,956 | 2,955 | -0.0% | -9.88 to 7.22 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.32 | 0.32 | +0.0% | -0.0149 to 0.0149 | EVEN, the same |
| latency, 99th percentile (ms) | 0.448 | 0.443 | -1.2% | -0.0168 to 0.00614 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.198 | +0.9% | 0.000939 to 0.00251 | LOSS |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 453 | -11.6% | -161 to 42.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 410 | -11.5% | -155 to 48.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,296 | 457,326 | +24.5% | -127,996 to 308,056 | shown, not judged |
| host CPU busy (share of the run) | 0.0958 | 0.0989 | +3.2% | -0.000376 to 0.00657 | EVEN, no difference beyond the noise |
| host CPU-seconds | 159 | 164 | +3.5% | -0.771 to 11.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.118 | 0.122 | +3.5% | -0.000199 to 0.0085 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11.7 |  | 10.2 to 13.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 8.12 | 5.01 | -38.3% | -10.4 to 4.16 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 984 | +0.1% | -3 to 5.22 | EVEN, no difference beyond the noise |
| queries a second | 983 | 984 | +0.1% | -3 to 5.22 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.87 | 1.96 | +4.8% | -0.269 to 0.449 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.91 | 4.01 | +2.5% | -0.277 to 0.47 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.1 | 1.12 | +1.9% | -0.0942 to 0.135 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 502 | -1.9% | -87 to 67.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 432 | -4.7% | -116 to 73.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,430 | 199,199 | +5.2% | -73,049 to 92,588 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.127 | +5.4% | -0.0418 to 0.0548 | EVEN, no difference beyond the noise |
| host CPU-seconds | 185 | 195 | +5.4% | -64.5 to 84.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 50.4 | 108 | +114.3% | -109 to 224 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.3 |  | -0.964 to 37.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
