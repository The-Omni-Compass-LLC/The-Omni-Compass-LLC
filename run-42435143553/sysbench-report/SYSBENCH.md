# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 292 | +0.5% | -4.64 to 7.55 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 293 | 295 | +0.6% | -4.37 to 7.94 | STEADY, no difference beyond the noise |
| queries a second | 4,693 | 4,722 | +0.6% | -69.9 to 127 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.46 | 5.57 | +2.1% | -0.706 to 0.939 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.05 | 8.28 | +2.9% | -0.467 to 0.931 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.3 | 3.3 | -0.1% | -0.0323 to 0.0251 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 948 | +85.1% | 43.5 to 828 | power given |
| pages holding data, mean (MB) | 457 | 841 | +84.1% | 110 to 659 | power given |
| pages read from disk into the pool (misses) | 249,164 | 121,276 | -51.3% | -231,924 to -23,851 | shown, not judged |
| host CPU busy (share of the run) | 0.256 | 0.258 | +0.7% | -0.0154 to 0.0191 | STEADY, no difference beyond the noise |
| host CPU-seconds | 152 | 153 | +0.6% | -9.66 to 11.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.42 | 3.42 | +0.2% | -0.168 to 0.185 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | +0.1% | -1.87 to 2.55 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.1% | -1.62 to 2.1 | STEADY, no difference beyond the noise |
| queries a second | 4,715 | 4,718 | +0.1% | -26 to 33.6 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.39 | 2.36 | -1.2% | -0.0882 to 0.0322 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.7 | 3.64 | -1.8% | -0.0678 to -0.0649 | GAIN |
| latency, mean (ms) | 1.75 | 1.74 | -0.9% | -0.0443 to 0.0125 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 462 | 458 | -0.7% | -17.4 to 11 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 656,806 | 656,665 | -0.0% | -13,098 to 12,816 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.147 | -0.4% | -0.00368 to 0.0026 | STEADY, no difference beyond the noise |
| host CPU-seconds | 269 | 268 | -0.4% | -7.09 to 5.07 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.99 | 1.98 | -0.5% | -0.0453 to 0.0261 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 181 | 184 | +1.6% | -4.26 to 10 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 198 | 198 | +0.1% | -1.07 to 1.65 | STEADY, no difference beyond the noise |
| queries a second | 3,951 | 3,957 | +0.1% | -21.5 to 32.9 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 26.8 | 26.2 | -2.4% | -12.6 to 11.3 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 169 | 119 | -29.6% | -114 to 14.3 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 9.87 | 8.27 | -16.3% | -3.81 to 0.604 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,232 | +140.7% | 679 to 762 | power given |
| pages holding data, mean (MB) | 463 | 1,021 | +120.7% | 538 to 579 | power given |
| pages read from disk into the pool (misses) | 619,704 | 91,266 | -85.3% | -572,870 to -484,006 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.17 | -8.7% | -0.0201 to -0.0122 | GAIN |
| host CPU-seconds | 329 | 301 | -8.7% | -35 to -22.2 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.98 | 3.58 | -10.1% | -0.454 to -0.35 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 4.87 to 12.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 8.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,961 | 2,961 | -0.0% | -6.72 to 6.43 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,966 | 2,966 | -0.0% | -9.74 to 9.14 | STEADY, no difference beyond the noise |
| queries a second | 2,966 | 2,966 | -0.0% | -9.74 to 9.14 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.161 | 0.152 | -5.6% | -0.0701 to 0.0521 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.328 | 0.33 | +0.7% | -0.0447 to 0.0494 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0831 | 0.0798 | -4.0% | -0.0235 to 0.0169 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 692 | +35.3% | -459 to 820 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 611 | +31.6% | -367 to 660 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,641 | 261,432 | -29.1% | -460,349 to 245,931 | shown, not judged |
| host CPU busy (share of the run) | 0.0662 | 0.0638 | -3.7% | -0.0139 to 0.00909 | STEADY, no difference beyond the noise |
| host CPU-seconds | 118 | 114 | -3.6% | -24.6 to 16.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0877 | 0.0845 | -3.6% | -0.0181 to 0.0118 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.33 |  | -5.65 to 10.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 92.3 | 102 | +10.6% | -54.6 to 74.2 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 981 | 979 | -0.2% | -6.81 to 3.25 | STEADY, no difference beyond the noise |
| queries a second | 981 | 979 | -0.2% | -6.81 to 3.25 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.31 | 1.27 | -2.7% | -0.289 to 0.219 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.01 | 1.93 | -3.9% | -0.694 to 0.539 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.876 | 0.86 | -1.8% | -0.128 to 0.0959 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.4% | 700 to 747 | power given |
| pages holding data, mean (MB) | 456 | 889 | +95.0% | 405 to 461 | power given |
| pages read from disk into the pool (misses) | 190,232 | 71,848 | -62.2% | -129,221 to -107,547 | shown, not judged |
| host CPU busy (share of the run) | 0.21 | 0.204 | -2.8% | -0.0384 to 0.0267 | STEADY, no difference beyond the noise |
| host CPU-seconds | 382 | 371 | -2.8% | -69.3 to 48.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 9.85 | 8.04 | -18.4% | -11.8 to 8.21 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
