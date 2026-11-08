# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 295 | +0.6% | -2.02 to 5.28 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.5% | -1.91 to 4.97 | STEADY, no difference beyond the noise |
| queries a second | 4,700 | 4,724 | +0.5% | -30.5 to 79.6 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.86 | 4.85 | -0.0% | -0.216 to 0.212 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.83 | 6.71 | -1.8% | -0.649 to 0.4 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.2 | 3.15 | -1.7% | -0.105 to -0.0019 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 827 | +61.6% | -183 to 814 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 457 | 721 | +57.6% | -42.5 to 569 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,682 | 155,477 | -36.7% | -192,547 to 12,138 | shown, not judged |
| host CPU busy (share of the run) | 0.247 | 0.244 | -1.0% | -0.00356 to -0.00135 | GAIN |
| host CPU-seconds | 147 | 145 | -1.0% | -2.04 to -0.889 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.27 | 3.22 | -1.5% | -0.0911 to -0.00975 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 1.33 |  | -0.101 to 2.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 294 | +0.6% | -4.56 to 8.14 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.2% | -1.92 to 3.1 | STEADY, no difference beyond the noise |
| queries a second | 4,742 | 4,751 | +0.2% | -30.8 to 49.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.73 | 2.55 | -6.4% | -0.361 to 0.0114 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 17.2 | 6.42 | -62.7% | -54.5 to 33 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.69 | 2.44 | -9.3% | -1.14 to 0.646 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,183 | +131.1% | 587 to 755 | power given |
| pages holding data, mean (MB) | 464 | 957 | +106.4% | 482 to 505 | power given |
| pages read from disk into the pool (misses) | 653,826 | 85,954 | -86.9% | -591,632 to -544,112 | shown, not judged |
| host CPU busy (share of the run) | 0.16 | 0.155 | -3.2% | -0.00974 to -0.000436 | GAIN |
| host CPU-seconds | 286 | 277 | -3.2% | -17.3 to -0.975 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.15 | 2.07 | -3.8% | -0.108 to -0.0535 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 12 |  | 7.7 to 16.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 4.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 188 | 189 | +0.7% | -7.48 to 10.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.1% | -3.59 to 3.14 | STEADY, no difference beyond the noise |
| queries a second | 3,943 | 3,938 | -0.1% | -71.8 to 62.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 12.2 | 6.97 | -42.7% | -20.3 to 9.92 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 605 | 108 | -82.1% | -2,414 to 1,421 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 17.3 | 6.64 | -61.7% | -50.1 to 28.7 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,156 | +125.7% | 439 to 849 | power given |
| pages holding data, mean (MB) | 462 | 977 | +111.4% | 390 to 640 | power given |
| pages read from disk into the pool (misses) | 618,720 | 125,056 | -79.8% | -568,474 to -418,854 | shown, not judged |
| host CPU busy (share of the run) | 0.183 | 0.17 | -6.9% | -0.0203 to -0.0049 | GAIN |
| host CPU-seconds | 324 | 302 | -6.8% | -35.3 to -8.54 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.78 | 3.5 | -7.4% | -0.528 to -0.0326 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | -0.606 to 16.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,935 | 2,936 | +0.0% | -12 to 13.2 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,943 | 2,943 | -0.0% | -10.9 to 10.6 | STEADY, no difference beyond the noise |
| queries a second | 2,943 | 2,943 | -0.0% | -10.9 to 10.6 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.278 | 0.274 | -1.7% | -0.0366 to 0.0273 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.508 | 0.502 | -1.2% | -0.0525 to 0.0405 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.179 | 0.177 | -1.2% | -0.0185 to 0.0141 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 552 | +7.8% | -131 to 211 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 497 | +7.1% | -132 to 198 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,283 | 344,207 | -6.5% | -119,141 to 70,989 | shown, not judged |
| host CPU busy (share of the run) | 0.152 | 0.151 | -0.8% | -0.0119 to 0.00955 | STEADY, no difference beyond the noise |
| host CPU-seconds | 275 | 273 | -0.8% | -21.1 to 16.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.204 | 0.202 | -0.8% | -0.0163 to 0.0131 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 5.1 | 6.65 | +30.5% | -0.494 to 3.61 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 984 | 983 | -0.1% | -1.23 to -0.771 | LOSS |
| queries a second | 984 | 983 | -0.1% | -1.23 to -0.771 | LOSS |
| latency, 95th percentile (ms) | 2.04 | 1.96 | -3.9% | -0.498 to 0.34 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.74 | 8.86 | +1.4% | -1.12 to 1.37 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.23 | 1.22 | -1.3% | -0.105 to 0.072 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,235 | +141.3% | 702 to 745 | power given |
| pages holding data, mean (MB) | 458 | 888 | +94.0% | 407 to 453 | power given |
| pages read from disk into the pool (misses) | 190,940 | 71,436 | -62.6% | -125,952 to -113,056 | shown, not judged |
| host CPU busy (share of the run) | 0.233 | 0.227 | -2.6% | -0.0347 to 0.0225 | STEADY, no difference beyond the noise |
| host CPU-seconds | 408 | 397 | -2.6% | -60 to 38.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 179 | 134 | -25.4% | -119 to 28.2 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
