# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 294 | +0.6% | -3.68 to 7.25 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 295 | +0.7% | -3.61 to 7.47 | EVEN, no difference beyond the noise |
| queries a second | 4,694 | 4,725 | +0.7% | -57.8 to 120 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.06 | 5.06 | -0.0% | -0.395 to 0.394 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.21 | 7.39 | +2.5% | -0.326 to 0.68 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.29 | 3.29 | +0.0% | -0.0505 to 0.0527 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 491 | -4.1% | -64 to 22.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 449 | 413 | -8.0% | -95 to 23.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 244,057 | 246,626 | +1.1% | -36,763 to 41,901 | shown, not judged |
| host CPU busy (share of the run) | 0.188 | 0.192 | +2.4% | -0.00401 to 0.0129 | EVEN, no difference beyond the noise |
| host CPU-seconds | 103 | 106 | +2.6% | -2.18 to 7.47 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.31 | 2.36 | +1.9% | -0.0447 to 0.133 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 3.7 to 12.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | +0.1% | -3.46 to 3.82 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.1% | -3.48 to 3.84 | EVEN, no difference beyond the noise |
| queries a second | 4,717 | 4,720 | +0.1% | -55.6 to 61.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.05 | 3.98 | -1.8% | -0.252 to 0.108 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.95 | 5.84 | -1.8% | -0.109 to -0.103 | GAIN |
| latency, mean (ms) | 3.11 | 3.09 | -0.6% | -0.0662 to 0.0302 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 520 | +1.7% | -4.35 to 21.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 467 | +1.1% | -5.9 to 16.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 653,221 | 614,507 | -5.9% | -53,990 to -23,438 | shown, not judged |
| host CPU busy (share of the run) | 0.181 | 0.181 | -0.3% | -0.00524 to 0.00417 | EVEN, no difference beyond the noise |
| host CPU-seconds | 300 | 300 | -0.2% | -8.73 to 7.36 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.23 | 2.23 | -0.3% | -0.0752 to 0.0621 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15.3 |  | 5.29 to 25.4 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 190 | +0.1% | -1.69 to 2.01 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.2% | -0.706 to -0.00714 | LOSS |
| queries a second | 3,928 | 3,921 | -0.2% | -14.1 to -0.143 | LOSS |
| latency, 95th percentile (ms) | 9.45 | 9.22 | -2.4% | -0.71 to 0.259 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 14.3 | 14 | -2.0% | -3.69 to 3.13 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.79 | 5.56 | -4.0% | -1.54 to 1.08 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 571 | +11.5% | -24.2 to 142 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 502 | +8.5% | -30.3 to 109 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 615,623 | 532,653 | -13.5% | -225,646 to 59,706 | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.21 | -2.6% | -0.0155 to 0.00439 | EVEN, no difference beyond the noise |
| host CPU-seconds | 348 | 339 | -2.5% | -24.7 to 7.36 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.99 | 3.89 | -2.5% | -0.287 to 0.0836 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | 13.5 to 19.2 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,945 | 2,946 | +0.1% | -11 to 14.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,954 | +0.1% | -10.6 to 14.8 | EVEN, no difference beyond the noise |
| queries a second | 2,952 | 2,954 | +0.1% | -10.6 to 14.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.357 | 0.354 | -0.7% | -0.0124 to 0.00771 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.484 | 0.478 | -1.2% | -0.0301 to 0.0187 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.217 | 0.219 | +1.0% | -0.00613 to 0.0107 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 476 | -7.1% | -92 to 19.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 434 | -6.5% | -84.8 to 24.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,730 | 395,359 | +7.8% | -58,019 to 115,277 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.117 | +0.9% | -0.00179 to 0.00387 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 194 | +1.0% | -2.22 to 5.91 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.144 | +0.9% | -0.00149 to 0.00408 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.3 |  | 5.35 to 21.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 196 | 209 | +6.5% | -57 to 82.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 987 | 988 | +0.1% | -8.42 to 10.6 | EVEN, no difference beyond the noise |
| queries a second | 987 | 988 | +0.1% | -8.42 to 10.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.31 | 3.06 | -29.0% | -1.85 to -0.648 | GAIN |
| latency, 99th percentile (ms) | 13.3 | 9.93 | -25.6% | -9.68 to 2.87 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.53 | 1.26 | -17.7% | -0.523 to -0.016 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 361 | -29.5% | -232 to -69.7 | GAIN |
| pages holding data, mean (MB) | 453 | 290 | -36.0% | -243 to -82.8 | GAIN |
| pages read from disk into the pool (misses) | 189,003 | 287,191 | +52.0% | 86,916 to 109,461 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.119 | +2.5% | -0.0113 to 0.017 | EVEN, no difference beyond the noise |
| host CPU-seconds | 205 | 211 | +2.5% | -19.7 to 29.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.35 | 2.24 | -4.8% | -1.18 to 0.951 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16 |  | 7.04 to 25 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
