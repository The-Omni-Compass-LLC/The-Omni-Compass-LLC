# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 282 | 283 | +0.4% | -19.4 to 21.5 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.6% | -10.9 to 7.34 | STEADY, no difference beyond the noise |
| queries a second | 4,759 | 4,730 | -0.6% | -175 to 117 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 14 | 6.97 | -50.0% | -43.2 to 29.2 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 305 | 252 | -17.3% | -183 to 77.5 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 10.5 | 8.18 | -22.0% | -7.69 to 3.08 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,260 | +146.2% | 606 to 891 | power given |
| pages holding data, mean (MB) | 453 | 974 | +114.9% | 466 to 575 | power given |
| pages read from disk into the pool (misses) | 243,848 | 81,377 | -66.6% | -172,799 to -152,142 | shown, not judged |
| host CPU busy (share of the run) | 0.17 | 0.164 | -3.5% | -0.0131 to 0.00104 | STEADY, no difference beyond the noise |
| host CPU-seconds | 102 | 98.2 | -3.6% | -7.75 to 0.468 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.37 | 2.28 | -3.9% | -0.308 to 0.123 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.67 |  | -0.585 to 11.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 297 | +0.1% | -1.73 to 2.53 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 297 | +0.1% | -1.71 to 2.38 | STEADY, no difference beyond the noise |
| queries a second | 4,744 | 4,750 | +0.1% | -27.4 to 38 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.17 | 1.94 | -10.6% | -0.652 to 0.193 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.23 | 3.98 | -5.8% | -0.345 to -0.147 | GAIN |
| latency, mean (ms) | 1.31 | 1.27 | -3.0% | -0.243 to 0.165 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 462 | 458 | -0.7% | -16.1 to 9.98 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,418 | 655,951 | +0.1% | -3,539 to 4,604 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.103 | -2.1% | -0.02 to 0.0155 | STEADY, no difference beyond the noise |
| host CPU-seconds | 189 | 185 | -2.1% | -35.9 to 28 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.4 | 1.37 | -2.2% | -0.269 to 0.207 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 174 | 167 | -4.1% | -20.2 to 6.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.1% | -2.31 to 2.9 | STEADY, no difference beyond the noise |
| queries a second | 3,943 | 3,949 | +0.1% | -46.1 to 58 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 45.2 | 86.7 | +91.6% | 7.27 to 75.6 | LOSS |
| latency, 99th percentile (ms) | 146 | 245 | +68.0% | 54.6 to 144 | LOSS |
| latency, mean (ms) | 10.2 | 16.6 | +62.2% | 2.77 to 9.94 | LOSS |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,256 | +145.3% | 705 to 783 | power given |
| pages holding data, mean (MB) | 463 | 1,027 | +121.6% | 544 to 583 | power given |
| pages read from disk into the pool (misses) | 617,848 | 83,314 | -86.5% | -571,698 to -497,372 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.168 | -9.4% | -0.0202 to -0.0147 | GAIN |
| host CPU-seconds | 329 | 298 | -9.3% | -35.5 to -25.8 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.15 | 3.92 | -5.6% | -0.509 to 0.0441 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 |  | 6.08 to 18.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 10.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,949 | 2,948 | -0.1% | -12 to 9.04 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,955 | 2,953 | -0.0% | -10.5 to 7.78 | STEADY, no difference beyond the noise |
| queries a second | 2,955 | 2,953 | -0.0% | -10.5 to 7.78 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.301 | 0.301 | -0.1% | -0.014 to 0.0133 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.437 | 0.435 | -0.6% | -0.0141 to 0.00881 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.189 | 0.19 | +0.2% | -0.00212 to 0.00297 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 464 | 461 | -0.7% | -16.7 to 10.2 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,204 | 365,778 | -0.7% | -12,605 to 7,752 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.154 | +0.5% | -0.000651 to 0.00228 | STEADY, no difference beyond the noise |
| host CPU-seconds | 269 | 271 | +0.5% | -1.2 to 4.05 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.2 | 0.201 | +0.6% | -0.00154 to 0.0038 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 147 | 144 | -2.0% | -79.6 to 73.9 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 987 | 988 | +0.2% | -2.32 to 5.52 | STEADY, no difference beyond the noise |
| queries a second | 987 | 988 | +0.2% | -2.32 to 5.52 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 12.6 | 56.4 | +348.7% | -18.9 to 107 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 71.2 | 172 | +141.1% | 44.6 to 156 | LOSS |
| latency, mean (ms) | 4.02 | 9.87 | +145.6% | 1.21 to 10.5 | LOSS |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,213 | +136.8% | 647 to 754 | power given |
| pages holding data, mean (MB) | 456 | 892 | +95.8% | 403 to 470 | power given |
| pages read from disk into the pool (misses) | 192,764 | 69,538 | -63.9% | -137,786 to -108,665 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.136 | -4.5% | -0.0263 to 0.0135 | STEADY, no difference beyond the noise |
| host CPU-seconds | 249 | 238 | -4.3% | -45.5 to 24.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.96 | 3.65 | -7.8% | -3.44 to 2.82 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
