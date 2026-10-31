# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.2% | -5.91 to 4.6 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.2% | -5.67 to 4.27 | EVEN, no difference beyond the noise |
| queries a second | 4,725 | 4,714 | -0.2% | -90.7 to 68.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.8 | 4.71 | -1.8% | -0.0905 to -0.0802 | GAIN |
| latency, 99th percentile (ms) | 6.83 | 6.67 | -2.4% | -0.323 to 0.00141 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.13 | 3.11 | -0.6% | -0.0835 to 0.0443 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 712 | +39.0% | 197 to 203 | power given |
| pages holding data, mean (MB) | 451 | 642 | +42.5% | 186 to 198 | power given |
| pages read from disk into the pool (misses) | 247,037 | 181,889 | -26.4% | -71,068 to -59,228 | shown, not judged |
| host CPU busy (share of the run) | 0.242 | 0.24 | -0.6% | -0.00213 to -0.000553 | GAIN |
| host CPU-seconds | 144 | 143 | -0.6% | -1.22 to -0.434 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.19 | 3.18 | -0.4% | -0.0614 to 0.038 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.3% | -1.51 to 3.32 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.3% | -2.11 to 3.64 | EVEN, no difference beyond the noise |
| queries a second | 4,682 | 4,695 | +0.3% | -33.7 to 58.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.74 | 2.76 | +0.6% | -0.127 to 0.16 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.63 | 4.54 | -1.9% | -0.644 to 0.471 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.82 | 2.11 | -25.3% | -3.73 to 2.31 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 753 | +47.2% | 183 to 300 | power given |
| pages holding data, mean (MB) | 463 | 647 | +39.9% | 173 to 196 | power given |
| pages read from disk into the pool (misses) | 654,812 | 315,162 | -51.9% | -357,494 to -321,806 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.162 | -1.0% | -0.00831 to 0.00487 | EVEN, no difference beyond the noise |
| host CPU-seconds | 300 | 297 | -1.1% | -15.2 to 8.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.23 | 2.2 | -1.3% | -0.103 to 0.043 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | -1.5 to 8.84 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 196 | +2.7% | 3.51 to 6.9 | GAIN |
| throughput (transactions a second) | 196 | 197 | +0.3% | -0.639 to 1.78 | EVEN, no difference beyond the noise |
| queries a second | 3,924 | 3,936 | +0.3% | -12.8 to 35.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.11 | 7.08 | -22.3% | -2.44 to -1.62 | GAIN |
| latency, 99th percentile (ms) | 13.5 | 9.68 | -28.5% | -5.65 to -2.08 | GAIN |
| latency, mean (ms) | 5.38 | 5.09 | -5.4% | -0.623 to 0.0404 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,106 | +115.9% | 521 to 666 | power given |
| pages holding data, mean (MB) | 462 | 976 | +111.0% | 431 to 595 | power given |
| pages read from disk into the pool (misses) | 615,929 | 99,113 | -83.9% | -585,405 to -448,228 | shown, not judged |
| host CPU busy (share of the run) | 0.282 | 0.266 | -5.8% | -0.0222 to -0.0107 | GAIN |
| host CPU-seconds | 496 | 467 | -5.9% | -39.1 to -19.3 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.69 | 5.21 | -8.4% | -0.554 to -0.401 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 5.67 |  | 4.23 to 7.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,942 | 2,940 | -0.0% | -10.2 to 7.5 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,950 | 2,954 | +0.1% | -5.08 to 11.8 | EVEN, no difference beyond the noise |
| queries a second | 2,950 | 2,954 | +0.1% | -5.08 to 11.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.33 | 0.34 | +2.9% | -0.0453 to 0.0647 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.458 | 0.496 | +8.4% | -0.0458 to 0.123 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.194 | 0.194 | -0.2% | -0.031 to 0.0302 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 548 | +7.1% | -120 to 193 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 465 | 494 | +6.2% | -118 to 177 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,531 | 331,022 | -10.2% | -183,137 to 108,118 | shown, not judged |
| host CPU busy (share of the run) | 0.157 | 0.158 | +0.4% | -0.0173 to 0.0185 | EVEN, no difference beyond the noise |
| host CPU-seconds | 276 | 277 | +0.4% | -29.1 to 31.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.205 | 0.206 | +0.4% | -0.0223 to 0.0241 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 13 | 14.7 | +13.5% | -1.75 to 5.26 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 985 | +0.3% | -5.03 to 10 | EVEN, no difference beyond the noise |
| queries a second | 983 | 985 | +0.3% | -5.03 to 10 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.02 | 2 | -1.3% | -0.138 to 0.0859 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.51 | 5.51 | -0.1% | -0.248 to 0.242 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.14 | 1.13 | -0.6% | -0.0433 to 0.0294 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,239 | +141.9% | 695 to 758 | power given |
| pages holding data, mean (MB) | 458 | 891 | +94.5% | 406 to 460 | power given |
| pages read from disk into the pool (misses) | 192,723 | 71,821 | -62.7% | -127,893 to -113,913 | shown, not judged |
| host CPU busy (share of the run) | 0.239 | 0.234 | -1.9% | -0.0295 to 0.0204 | EVEN, no difference beyond the noise |
| host CPU-seconds | 419 | 411 | -1.9% | -51.1 to 35.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 78.2 | 64 | -18.1% | -62.7 to 34.4 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
