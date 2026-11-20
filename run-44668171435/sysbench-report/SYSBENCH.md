# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 294 | +0.5% | -2.11 to 4.81 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 293 | 295 | +0.5% | -2.36 to 5.13 | STEADY, no difference beyond the noise |
| queries a second | 4,694 | 4,716 | +0.5% | -37.7 to 82 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.23 | 4.18 | -1.2% | -0.161 to 0.0587 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.99 | 5.85 | -2.4% | -0.307 to 0.0206 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.7 | 2.67 | -1.2% | -0.097 to 0.0348 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 678 | +32.5% | 22.5 to 310 | power given |
| pages holding data, mean (MB) | 452 | 611 | +35.3% | 22.6 to 296 | power given |
| pages read from disk into the pool (misses) | 244,134 | 192,120 | -21.3% | -93,977 to -10,051 | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.221 | +0.2% | -0.00663 to 0.00772 | STEADY, no difference beyond the noise |
| host CPU-seconds | 132 | 132 | +0.1% | -4.13 to 4.47 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.94 | 2.94 | -0.2% | -0.0672 to 0.0539 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 297 | 296 | -0.3% | -2.3 to 0.707 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.2% | -1.85 to 0.643 | STEADY, no difference beyond the noise |
| queries a second | 4,753 | 4,744 | -0.2% | -29.5 to 10.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.65 | 1.64 | -0.4% | -0.162 to 0.148 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.13 | 3.36 | +7.2% | -0.984 to 1.43 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.15 | 1.16 | +0.7% | -0.0873 to 0.103 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 688 | +34.3% | -204 to 555 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 610 | +31.4% | -175 to 466 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,962 | 447,010 | -31.9% | -661,443 to 243,538 | shown, not judged |
| host CPU busy (share of the run) | 0.0937 | 0.0935 | -0.2% | -0.0022 to 0.0019 | STEADY, no difference beyond the noise |
| host CPU-seconds | 168 | 168 | -0.1% | -3.99 to 3.52 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.25 | 1.25 | +0.1% | -0.0333 to 0.0361 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | -4.92 to 10.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 158 | 159 | +1.0% | -23.7 to 26.7 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.1% | -1.27 to 1.76 | STEADY, no difference beyond the noise |
| queries a second | 3,935 | 3,940 | +0.1% | -25.3 to 35.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 95.8 | 85.8 | -10.4% | -60.9 to 40.9 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 229 | 231 | +0.7% | -161 to 164 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 18.1 | 17.5 | -3.0% | -14.1 to 13 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,248 | +143.8% | 706 to 766 | power given |
| pages holding data, mean (MB) | 463 | 1,026 | +121.6% | 541 to 585 | power given |
| pages read from disk into the pool (misses) | 615,446 | 85,156 | -86.2% | -569,014 to -491,566 | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.183 | -7.1% | -0.0249 to -0.00291 | GAIN |
| host CPU-seconds | 349 | 324 | -7.1% | -44.2 to -5.24 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.85 | 4.48 | -7.7% | -1.1 to 0.356 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9 |  | 4.03 to 14 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 7.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,960 | 2,961 | +0.0% | -9.69 to 12.3 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,968 | 2,968 | -0.0% | -11.4 to 11.2 | STEADY, no difference beyond the noise |
| queries a second | 2,968 | 2,968 | -0.0% | -11.4 to 11.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.21 | 0.197 | -6.3% | -0.0283 to 0.00164 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.352 | 0.344 | -2.3% | -0.0308 to 0.0148 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.181 | 0.191 | +5.9% | -0.0736 to 0.095 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,127 | +120.2% | 511 to 719 | power given |
| pages holding data, mean (MB) | 466 | 915 | +96.2% | 441 to 456 | power given |
| pages read from disk into the pool (misses) | 368,497 | 78,326 | -78.7% | -301,518 to -278,824 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.109 | -2.4% | -0.00306 to -0.00233 | GAIN |
| host CPU-seconds | 198 | 193 | -2.4% | -5.28 to -4.22 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 0.147 | 0.143 | -2.5% | -0.00431 to -0.00289 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 5.67 |  | 0.495 to 10.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 5.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 98.1 | 121 | +23.6% | -60 to 106 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 988 | 988 | -0.1% | -4.03 to 2.51 | STEADY, no difference beyond the noise |
| queries a second | 988 | 988 | -0.1% | -4.03 to 2.51 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 78.7 | 107 | +35.9% | -30 to 86.5 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 201 | 299 | +48.8% | -186 to 382 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 13.2 | 18.9 | +43.2% | -4.81 to 16.2 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,226 | +139.4% | 689 to 739 | power given |
| pages holding data, mean (MB) | 456 | 892 | +95.4% | 405 to 466 | power given |
| pages read from disk into the pool (misses) | 193,390 | 71,407 | -63.1% | -130,765 to -113,202 | shown, not judged |
| host CPU busy (share of the run) | 0.152 | 0.14 | -7.9% | -0.0317 to 0.00779 | STEADY, no difference beyond the noise |
| host CPU-seconds | 267 | 246 | -7.8% | -54.8 to 13.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 6.1 | 4.81 | -21.1% | -5.44 to 2.86 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
