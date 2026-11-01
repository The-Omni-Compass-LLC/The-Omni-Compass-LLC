# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | -0.0% | -6.56 to 6.45 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.1% | -5.69 to 5.32 | STEADY, no difference beyond the noise |
| queries a second | 4,700 | 4,697 | -0.1% | -91.1 to 85.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.64 | 3.57 | -1.9% | -0.554 to 0.417 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 35.6 | 5.78 | -83.7% | -159 to 99.4 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.03 | 2.26 | -25.5% | -4.81 to 3.27 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 490 | +282.5% | 172 to 551 | power given |
| pages holding data, mean (MB) | 121 | 442 | +266.7% | 77.2 to 566 | power given |
| pages read from disk into the pool (misses) | 599,656 | 288,306 | -51.9% | -376,330 to -246,370 | shown, not judged |
| host CPU busy (share of the run) | 0.167 | 0.162 | -2.6% | -0.0098 to 0.00116 | STEADY, no difference beyond the noise |
| host CPU-seconds | 102 | 99.2 | -2.6% | -6.12 to 0.878 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.27 | 2.21 | -2.6% | -0.182 to 0.0655 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.67 |  | -1.2 to 4.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 3.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.2% | -2.97 to 1.73 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | -0.1% | -2.97 to 2.4 | STEADY, no difference beyond the noise |
| queries a second | 4,739 | 4,735 | -0.1% | -47.5 to 38.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.69 | 2.6 | -3.5% | -0.213 to 0.0233 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.31 | 4.47 | +3.7% | -0.0518 to 0.37 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.3 | 2.22 | -3.5% | -0.247 to 0.0853 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,099 | +758.9% | 812 to 1,130 | power given |
| pages holding data, mean (MB) | 120 | 924 | +668.0% | 723 to 885 | power given |
| pages read from disk into the pool (misses) | 2,013,277 | 173,846 | -91.4% | -2,102,443 to -1,576,420 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.154 | -5.6% | -0.0171 to -0.000983 | GAIN |
| host CPU-seconds | 290 | 274 | -5.5% | -31.4 to -0.484 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.16 | 2.05 | -5.3% | -0.224 to -0.00509 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 11 |  | 0.171 to 21.8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 3.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 195 | +1.1% | 1.6 to 2.72 | GAIN |
| throughput (transactions a second) | 195 | 196 | +0.3% | -0.699 to 1.71 | STEADY, no difference beyond the noise |
| queries a second | 3,900 | 3,911 | +0.3% | -14 to 34.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 7.99 | 5.95 | -25.5% | -2.59 to -1.47 | GAIN |
| latency, 99th percentile (ms) | 10.8 | 8.48 | -21.3% | -3.51 to -1.08 | GAIN |
| latency, mean (ms) | 4.37 | 3.92 | -10.4% | -0.575 to -0.337 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 563 | +339.8% | 288 to 582 | power given |
| pages holding data, mean (MB) | 121 | 516 | +325.9% | 262 to 527 | power given |
| pages read from disk into the pool (misses) | 1,656,062 | 547,478 | -66.9% | -1,355,358 to -861,809 | shown, not judged |
| host CPU busy (share of the run) | 0.246 | 0.224 | -9.1% | -0.0281 to -0.0166 | GAIN |
| host CPU-seconds | 448 | 407 | -9.1% | -50.8 to -31 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.06 | 4.54 | -10.1% | -0.613 to -0.409 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,953 | 2,961 | +0.3% | -26 to 42.4 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,966 | +0.0% | -8.96 to 10.1 | STEADY, no difference beyond the noise |
| queries a second | 2,965 | 2,966 | +0.0% | -8.96 to 10.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.234 | 0.205 | -12.5% | -0.0707 to 0.012 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.366 | 0.35 | -4.3% | -0.0847 to 0.0534 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.477 | 0.186 | -60.9% | -1.06 to 0.477 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,037 | +710.1% | 755 to 1,062 | power given |
| pages holding data, mean (MB) | 121 | 859 | +608.2% | 641 to 834 | power given |
| pages read from disk into the pool (misses) | 1,031,256 | 116,407 | -88.7% | -997,357 to -832,339 | shown, not judged |
| host CPU busy (share of the run) | 0.115 | 0.107 | -6.4% | -0.00955 to -0.00516 | GAIN |
| host CPU-seconds | 204 | 191 | -6.4% | -17 to -9.18 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 0.152 | 0.141 | -6.7% | -0.014 to -0.0062 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 1.08 to 16.3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 3.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 12.8 | 20.8 | +62.9% | 4.53 to 11.5 | GAIN |
| throughput (transactions a second) | 985 | 982 | -0.2% | -4.52 to 0.372 | STEADY, no difference beyond the noise |
| queries a second | 985 | 982 | -0.2% | -4.52 to 0.372 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.2 | 1.74 | -20.9% | -0.599 to -0.321 | GAIN |
| latency, 99th percentile (ms) | 3.86 | 3.59 | -7.0% | -0.443 to -0.0949 | GAIN |
| latency, mean (ms) | 1.13 | 1.03 | -8.4% | -0.168 to -0.022 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,284 | +902.8% | 1,084 to 1,227 | power given |
| pages holding data, mean (MB) | 118 | 873 | +637.3% | 719 to 789 | power given |
| pages read from disk into the pool (misses) | 418,220 | 77,896 | -81.4% | -355,097 to -325,550 | shown, not judged |
| host CPU busy (share of the run) | 0.25 | 0.218 | -13.1% | -0.0602 to -0.00519 | GAIN |
| host CPU-seconds | 439 | 382 | -13.0% | -105 to -9.8 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 87.7 | 41.2 | -53.0% | -146 to 53.1 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
