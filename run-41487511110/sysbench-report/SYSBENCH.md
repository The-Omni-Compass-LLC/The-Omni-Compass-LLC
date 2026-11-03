# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 295 | +0.8% | -4.98 to 9.89 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 293 | 295 | +0.8% | -5.24 to 10.1 | STEADY, no difference beyond the noise |
| queries a second | 4,686 | 4,725 | +0.8% | -83.9 to 162 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.18 | 4.2 | +0.6% | -0.264 to 0.315 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.88 | 5.91 | +0.6% | -0.271 to 0.341 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.7 | 2.7 | -0.1% | -0.0756 to 0.0722 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 679 | +32.6% | 21.8 to 312 | power given |
| pages holding data, mean (MB) | 452 | 610 | +35.0% | 25.1 to 291 | power given |
| pages read from disk into the pool (misses) | 246,201 | 192,370 | -21.9% | -90,053 to -17,610 | shown, not judged |
| host CPU busy (share of the run) | 0.215 | 0.217 | +0.7% | -0.00563 to 0.0086 | STEADY, no difference beyond the noise |
| host CPU-seconds | 129 | 130 | +0.7% | -3.55 to 5.38 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.88 | 2.87 | -0.1% | -0.102 to 0.0955 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.4% | -7.29 to 9.51 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 297 | -0.0% | -2.26 to 1.98 | STEADY, no difference beyond the noise |
| queries a second | 4,748 | 4,745 | -0.0% | -36.1 to 31.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.79 | 2.65 | -5.3% | -0.273 to -0.0218 | GAIN |
| latency, 99th percentile (ms) | 29.9 | 13.8 | -53.9% | -105 to 73.2 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.02 | 2.67 | -11.6% | -2.93 to 2.23 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,193 | +133.0% | 469 to 892 | power given |
| pages holding data, mean (MB) | 461 | 960 | +108.0% | 487 to 510 | power given |
| pages read from disk into the pool (misses) | 658,615 | 79,723 | -87.9% | -582,843 to -574,941 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.158 | -3.4% | -0.00984 to -0.00122 | GAIN |
| host CPU-seconds | 294 | 284 | -3.4% | -17.6 to -2.23 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.21 | 2.12 | -3.7% | -0.139 to -0.0255 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 |  | 1.99 to 22.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 5.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 196 | 195 | -0.1% | -1.82 to 1.25 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.3% | -2.79 to 1.45 | STEADY, no difference beyond the noise |
| queries a second | 3,929 | 3,915 | -0.3% | -55.7 to 29 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.63 | 5.88 | -11.3% | -1.17 to -0.329 | GAIN |
| latency, 99th percentile (ms) | 9.33 | 8.03 | -13.9% | -1.87 to -0.728 | GAIN |
| latency, mean (ms) | 4.28 | 4.21 | -1.8% | -0.284 to 0.125 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 923 | +80.2% | 71.2 to 750 | power given |
| pages holding data, mean (MB) | 461 | 826 | +79.1% | 66.5 to 663 | power given |
| pages read from disk into the pool (misses) | 619,556 | 209,079 | -66.3% | -525,983 to -294,971 | shown, not judged |
| host CPU busy (share of the run) | 0.244 | 0.237 | -3.0% | -0.0136 to -0.000789 | GAIN |
| host CPU-seconds | 443 | 430 | -3.1% | -23.4 to -3.84 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.93 | 4.79 | -2.9% | -0.22 to -0.0694 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,947 | 2,945 | -0.0% | -27.4 to 24.5 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,967 | 2,963 | -0.1% | -12.5 to 4.68 | STEADY, no difference beyond the noise |
| queries a second | 2,967 | 2,963 | -0.1% | -12.5 to 4.68 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.263 | 0.234 | -11.0% | -0.0897 to 0.0317 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.438 | 0.404 | -7.8% | -0.326 to 0.257 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.597 | 0.474 | -20.5% | -1.06 to 0.816 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,144 | +123.4% | 513 to 750 | power given |
| pages holding data, mean (MB) | 464 | 917 | +97.7% | 435 to 471 | power given |
| pages read from disk into the pool (misses) | 367,562 | 77,894 | -78.8% | -300,464 to -278,870 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.115 | -2.4% | -0.015 to 0.0094 | STEADY, no difference beyond the noise |
| host CPU-seconds | 209 | 204 | -2.4% | -26.7 to 16.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.156 | 0.152 | -2.3% | -0.0211 to 0.0139 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 0.929 to 12.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 7.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 15.3 | 18.1 | +18.4% | -3.1 to 8.74 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 984 | 983 | -0.1% | -2.79 to 1.04 | STEADY, no difference beyond the noise |
| queries a second | 984 | 983 | -0.1% | -2.79 to 1.04 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.34 | 2.39 | +2.3% | -0.21 to 0.318 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.74 | 9.39 | +7.5% | 0.205 to 1.11 | LOSS |
| latency, mean (ms) | 1.27 | 1.28 | +0.7% | -0.0803 to 0.0977 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.5% | 705 to 744 | power given |
| pages holding data, mean (MB) | 460 | 889 | +93.3% | 414 to 444 | power given |
| pages read from disk into the pool (misses) | 186,286 | 71,808 | -61.5% | -131,590 to -97,365 | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.206 | -3.1% | -0.0349 to 0.0219 | STEADY, no difference beyond the noise |
| host CPU-seconds | 373 | 362 | -3.0% | -61.1 to 38.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 56.2 | 43.8 | -22.0% | -49.8 to 25.1 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
