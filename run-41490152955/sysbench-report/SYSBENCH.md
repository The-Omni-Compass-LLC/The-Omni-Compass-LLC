# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.0% | -2.53 to 2.76 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.1% | -2.38 to 2.97 | STEADY, no difference beyond the noise |
| queries a second | 4,712 | 4,717 | +0.1% | -38 to 47.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.99 | 5 | +0.3% | -0.884 to 0.912 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.96 | 8.04 | +1.0% | -0.812 to 0.968 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.09 | 3.05 | -1.2% | -0.103 to 0.0258 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,041 | +103.3% | 357 to 701 | power given |
| pages holding data, mean (MB) | 457 | 930 | +103.3% | 377 to 567 | power given |
| pages read from disk into the pool (misses) | 248,627 | 95,867 | -61.4% | -187,043 to -118,478 | shown, not judged |
| host CPU busy (share of the run) | 0.234 | 0.23 | -1.7% | -0.00616 to -0.00158 | GAIN |
| host CPU-seconds | 139 | 137 | -1.9% | -3.5 to -1.67 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.11 | 3.06 | -1.7% | -0.0603 to -0.0481 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 1.67 |  | -1.2 to 4.54 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | +0.1% | -1.38 to 1.82 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.1% | -1.57 to 2 | STEADY, no difference beyond the noise |
| queries a second | 4,719 | 4,723 | +0.1% | -25.1 to 32.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.91 | 3.86 | -1.2% | -0.148 to 0.0542 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.28 | 5.15 | -2.4% | -0.258 to 0.00739 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.99 | 2.96 | -0.9% | -0.0966 to 0.0426 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 462 | 459 | -0.7% | -15.6 to 9.27 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 652,920 | 654,690 | +0.3% | -10,971 to 14,511 | shown, not judged |
| host CPU busy (share of the run) | 0.238 | 0.236 | -0.7% | -0.00782 to 0.00461 | STEADY, no difference beyond the noise |
| host CPU-seconds | 422 | 420 | -0.7% | -14 to 8.28 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.13 | 3.11 | -0.7% | -0.0979 to 0.0514 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 143 | 142 | -0.9% | -28.8 to 26.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.2% | -0.92 to 1.85 | STEADY, no difference beyond the noise |
| queries a second | 3,932 | 3,941 | +0.2% | -18.4 to 37 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 175 | 145 | -17.6% | -188 to 127 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 363 | 301 | -17.2% | -345 to 220 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 31.9 | 27.6 | -13.4% | -30.8 to 22.2 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,302 | +154.3% | 746 to 834 | power given |
| pages holding data, mean (MB) | 462 | 1,034 | +123.9% | 535 to 609 | power given |
| pages read from disk into the pool (misses) | 618,423 | 79,214 | -87.2% | -587,712 to -490,705 | shown, not judged |
| host CPU busy (share of the run) | 0.18 | 0.162 | -10.2% | -0.0194 to -0.0175 | GAIN |
| host CPU-seconds | 320 | 287 | -10.3% | -35.3 to -30.5 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.93 | 4.45 | -9.8% | -1.5 to 0.536 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 5.16 to 15.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 8.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,957 | 2,959 | +0.0% | -5.93 to 8.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,963 | 2,963 | -0.0% | -9.63 to 9.26 | STEADY, no difference beyond the noise |
| queries a second | 2,963 | 2,963 | -0.0% | -9.63 to 9.26 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.222 | 0.203 | -8.4% | -0.0511 to 0.0138 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.344 | 0.34 | -1.2% | -0.0126 to 0.00461 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.154 | 0.149 | -3.4% | -0.0548 to 0.0444 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,033 | +101.7% | 21.6 to 1,020 | power given |
| pages holding data, mean (MB) | 466 | 834 | +79.1% | 112 to 625 | power given |
| pages read from disk into the pool (misses) | 368,226 | 143,496 | -61.0% | -375,739 to -73,720 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.108 | -2.0% | -0.00655 to 0.00202 | STEADY, no difference beyond the noise |
| host CPU-seconds | 197 | 193 | -2.0% | -11.2 to 3.35 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.146 | 0.143 | -2.0% | -0.00818 to 0.00221 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.33 |  | -7.35 to 20 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 2.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 4.73 | 8.97 | +89.7% | -3.79 to 12.3 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 980 | 979 | -0.1% | -0.753 to -0.337 | LOSS |
| queries a second | 980 | 979 | -0.1% | -0.753 to -0.337 | LOSS |
| latency, 95th percentile (ms) | 1.94 | 1.85 | -4.7% | -0.6 to 0.418 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.28 | 4.21 | -1.6% | -0.891 to 0.751 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.16 | 1.12 | -3.7% | -0.181 to 0.0964 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,235 | +141.2% | 702 to 744 | power given |
| pages holding data, mean (MB) | 456 | 888 | +94.8% | 406 to 458 | power given |
| pages read from disk into the pool (misses) | 192,459 | 71,384 | -62.9% | -128,631 to -113,518 | shown, not judged |
| host CPU busy (share of the run) | 0.171 | 0.163 | -5.0% | -0.0281 to 0.0111 | STEADY, no difference beyond the noise |
| host CPU-seconds | 308 | 293 | -4.9% | -49.7 to 19.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 171 | 82.6 | -51.7% | -314 to 137 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
