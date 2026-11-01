# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | +0.1% | -4.17 to 4.55 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.1% | -4.7 to 4.3 | STEADY, no difference beyond the noise |
| queries a second | 4,710 | 4,707 | -0.1% | -75.2 to 68.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5 | 4.77 | -4.7% | -0.358 to -0.109 | GAIN |
| latency, 99th percentile (ms) | 7.17 | 6.79 | -5.2% | -0.668 to -0.0832 | GAIN |
| latency, mean (ms) | 3.17 | 3.12 | -1.4% | -0.0602 to -0.0296 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 712 | +39.1% | 198 to 202 | power given |
| pages holding data, mean (MB) | 452 | 642 | +42.2% | 189 to 192 | power given |
| pages read from disk into the pool (misses) | 243,921 | 182,422 | -25.2% | -64,633 to -58,365 | shown, not judged |
| host CPU busy (share of the run) | 0.243 | 0.243 | +0.0% | -0.00627 to 0.00652 | STEADY, no difference beyond the noise |
| host CPU-seconds | 145 | 145 | +0.0% | -3.64 to 3.77 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.22 | 3.22 | -0.0% | -0.0376 to 0.0366 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 294 | +0.6% | -0.557 to 4.21 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.1% | -1.83 to 1.14 | STEADY, no difference beyond the noise |
| queries a second | 4,744 | 4,739 | -0.1% | -29.3 to 18.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.84 | 2.57 | -9.7% | -0.4 to -0.15 | GAIN |
| latency, 99th percentile (ms) | 24.5 | 5.73 | -76.6% | -40.3 to 2.73 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.1 | 2.38 | -23.1% | -1.39 to -0.0462 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,197 | +133.8% | 518 to 852 | power given |
| pages holding data, mean (MB) | 465 | 967 | +108.1% | 469 to 535 | power given |
| pages read from disk into the pool (misses) | 657,109 | 82,363 | -87.5% | -589,358 to -560,136 | shown, not judged |
| host CPU busy (share of the run) | 0.167 | 0.158 | -5.4% | -0.0119 to -0.0063 | GAIN |
| host CPU-seconds | 300 | 283 | -5.4% | -21.6 to -11 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.25 | 2.12 | -6.0% | -0.163 to -0.108 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 11 |  | 2.39 to 19.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 2.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 189 | 194 | +2.6% | -0.102 to 9.8 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.1% | -3.22 to 2.82 | STEADY, no difference beyond the noise |
| queries a second | 3,935 | 3,931 | -0.1% | -64.3 to 56.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.79 | 7.26 | -25.9% | -3.15 to -1.93 | GAIN |
| latency, 99th percentile (ms) | 17.8 | 13.5 | -24.2% | -9.97 to 1.35 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 5.81 | 5.19 | -10.7% | -1.17 to -0.0705 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,177 | +129.8% | 580 to 749 | power given |
| pages holding data, mean (MB) | 461 | 1,003 | +117.4% | 528 to 555 | power given |
| pages read from disk into the pool (misses) | 620,354 | 92,602 | -85.1% | -560,059 to -495,445 | shown, not judged |
| host CPU busy (share of the run) | 0.283 | 0.261 | -7.7% | -0.0317 to -0.012 | GAIN |
| host CPU-seconds | 497 | 459 | -7.7% | -56.3 to -20.7 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.74 | 5.17 | -10.0% | -0.791 to -0.362 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,964 | 2,962 | -0.1% | -11.7 to 7.12 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,968 | 2,966 | -0.1% | -4.75 to 0.29 | STEADY, no difference beyond the noise |
| queries a second | 2,968 | 2,966 | -0.1% | -4.75 to 0.29 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.239 | 0.21 | -12.3% | -0.0784 to 0.0197 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.368 | 0.352 | -4.3% | -0.0551 to 0.0238 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.164 | 0.206 | +25.4% | -0.226 to 0.309 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,138 | +122.2% | 415 to 836 | power given |
| pages holding data, mean (MB) | 466 | 890 | +91.1% | 326 to 522 | power given |
| pages read from disk into the pool (misses) | 368,930 | 118,735 | -67.8% | -365,852 to -134,538 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.108 | -8.0% | -0.0206 to 0.00181 | STEADY, no difference beyond the noise |
| host CPU-seconds | 209 | 192 | -8.1% | -35.4 to 1.57 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.155 | 0.143 | -8.0% | -0.0265 to 0.00164 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 |  | -3.26 to 11.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 277 | 288 | +4.1% | -135 to 157 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 989 | 989 | +0.1% | -5.63 to 7.5 | STEADY, no difference beyond the noise |
| queries a second | 989 | 989 | +0.1% | -5.63 to 7.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.34 | 3.28 | -1.8% | -2.26 to 2.14 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.89 | 9.06 | +1.9% | -10.3 to 10.6 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 1.13 | -5.9% | -0.781 to 0.638 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.4% | 705 to 743 | power given |
| pages holding data, mean (MB) | 455 | 887 | +95.1% | 399 to 465 | power given |
| pages read from disk into the pool (misses) | 191,953 | 71,337 | -62.8% | -128,197 to -113,035 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.108 | -2.7% | -0.0233 to 0.0173 | STEADY, no difference beyond the noise |
| host CPU-seconds | 195 | 189 | -2.7% | -40.6 to 30.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.62 | 1.47 | -9.7% | -1.46 to 1.15 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
