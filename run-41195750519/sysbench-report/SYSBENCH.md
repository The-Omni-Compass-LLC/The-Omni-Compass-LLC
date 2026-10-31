# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.3% | -3.19 to 1.24 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.3% | -2.93 to 1.45 | EVEN, no difference beyond the noise |
| queries a second | 4,711 | 4,699 | -0.3% | -46.8 to 23.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.97 | 4.97 | -0.0% | -0.222 to 0.218 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.04 | 7.13 | +1.2% | -0.29 to 0.465 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.22 | 3.21 | -0.2% | -0.0991 to 0.0846 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 779 | +52.1% | 122 to 412 | power given |
| pages holding data, mean (MB) | 453 | 704 | +55.4% | 124 to 378 | power given |
| pages read from disk into the pool (misses) | 248,257 | 161,563 | -34.9% | -118,869 to -54,520 | shown, not judged |
| host CPU busy (share of the run) | 0.251 | 0.248 | -1.1% | -0.0136 to 0.00807 | EVEN, no difference beyond the noise |
| host CPU-seconds | 149 | 147 | -1.2% | -8.78 to 5.15 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.32 | 3.29 | -0.8% | -0.145 to 0.095 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | -0.3% | -3.53 to 1.95 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | -0.3% | -3.38 to 1.71 | EVEN, no difference beyond the noise |
| queries a second | 4,695 | 4,682 | -0.3% | -54.1 to 27.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.48 | 2.48 | -0.0% | -0.112 to 0.111 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.96 | 3.96 | +0.0% | -0.176 to 0.176 | EVEN, the same |
| latency, mean (ms) | 1.86 | 1.85 | -0.2% | -0.145 to 0.136 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 549 | +7.2% | -122 to 195 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 492 | +6.3% | -118 to 176 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 657,063 | 587,394 | -10.6% | -347,372 to 208,035 | shown, not judged |
| host CPU busy (share of the run) | 0.159 | 0.159 | +0.0% | -0.0114 to 0.0116 | EVEN, no difference beyond the noise |
| host CPU-seconds | 295 | 295 | +0.1% | -21.3 to 21.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.18 | 2.19 | +0.3% | -0.164 to 0.178 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 182 | 180 | -1.1% | -32.9 to 28.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 197 | -0.1% | -0.934 to 0.356 | EVEN, no difference beyond the noise |
| queries a second | 3,953 | 3,948 | -0.1% | -18.7 to 7.13 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 29.1 | 37.2 | +27.9% | -80.9 to 97.1 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 110 | 127 | +15.5% | -122 to 156 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 7.89 | 8.85 | +12.1% | -8.43 to 10.3 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,242 | +142.5% | 697 to 762 | power given |
| pages holding data, mean (MB) | 463 | 1,014 | +119.1% | 524 to 578 | power given |
| pages read from disk into the pool (misses) | 619,861 | 94,920 | -84.7% | -571,783 to -478,100 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.168 | -8.1% | -0.0213 to -0.00843 | GAIN |
| host CPU-seconds | 323 | 297 | -8.1% | -37 to -15.3 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.9 | 3.63 | -7.0% | -0.798 to 0.252 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 3.7 to 12.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 4.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,945 | 2,939 | -0.2% | -10.3 to -1.39 | LOSS |
| throughput (transactions a second) | 2,957 | 2,951 | -0.2% | -7.11 to -4.48 | LOSS |
| queries a second | 2,957 | 2,951 | -0.2% | -7.11 to -4.48 | LOSS |
| latency, 95th percentile (ms) | 0.353 | 0.346 | -1.8% | -0.0491 to 0.0364 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.502 | 0.493 | -1.7% | -0.046 to 0.0286 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.209 | 0.207 | -1.0% | -0.0124 to 0.00821 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 540 | +5.5% | -93.5 to 150 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 465 | 487 | +4.8% | -96.4 to 141 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,957 | 341,979 | -6.8% | -125,877 to 75,921 | shown, not judged |
| host CPU busy (share of the run) | 0.168 | 0.166 | -1.1% | -0.00939 to 0.00584 | EVEN, no difference beyond the noise |
| host CPU-seconds | 296 | 293 | -1.1% | -17 to 10.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.22 | 0.218 | -0.9% | -0.0121 to 0.00814 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 21.1 | 23.8 | +13.2% | -7.2 to 12.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 982 | 985 | +0.3% | -0.179 to 5.62 | EVEN, no difference beyond the noise |
| queries a second | 982 | 985 | +0.3% | -0.179 to 5.62 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.67 | 1.62 | -3.2% | -0.366 to 0.26 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.68 | 3.68 | +0.0% | -0.286 to 0.286 | EVEN, the same |
| latency, mean (ms) | 1.01 | 1 | -0.7% | -0.0946 to 0.08 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.4% | 702 to 746 | power given |
| pages holding data, mean (MB) | 457 | 889 | +94.5% | 411 to 453 | power given |
| pages read from disk into the pool (misses) | 192,730 | 71,608 | -62.8% | -130,912 to -111,332 | shown, not judged |
| host CPU busy (share of the run) | 0.224 | 0.219 | -2.1% | -0.0329 to 0.0236 | EVEN, no difference beyond the noise |
| host CPU-seconds | 393 | 385 | -2.1% | -57.6 to 41.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 42.9 | 35.4 | -17.4% | -38.3 to 23.4 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
