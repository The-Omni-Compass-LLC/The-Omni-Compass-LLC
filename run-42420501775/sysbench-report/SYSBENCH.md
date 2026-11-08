# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.3% | -6.38 to 4.5 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 296 | 295 | -0.2% | -6.45 to 5.12 | STEADY, no difference beyond the noise |
| queries a second | 4,730 | 4,720 | -0.2% | -103 to 82 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.9 | 2.9 | -0.1% | -0.39 to 0.386 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.36 | 4.54 | +4.2% | -0.309 to 0.674 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.47 | 1.45 | -1.6% | -0.0606 to 0.013 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 572 | +346.8% | -160 to 1,048 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 494 | +310.0% | -9.74 to 757 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 596,171 | 295,924 | -50.4% | -451,276 to -149,217 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.105 | -5.1% | -0.00898 to -0.00226 | GAIN |
| host CPU-seconds | 66.5 | 63.1 | -5.1% | -5.42 to -1.36 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 1.48 | 1.41 | -4.8% | -0.134 to -0.00724 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | -5.61 to 11.6 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.4% | -1.65 to 3.74 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.5% | -1.33 to 4.07 | STEADY, no difference beyond the noise |
| queries a second | 4,703 | 4,725 | +0.5% | -21.2 to 65.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.4 | 3.43 | +0.7% | -0.473 to 0.519 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.46 | 4.68 | +5.0% | -0.416 to 0.86 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.68 | 2.6 | -2.9% | -0.4 to 0.244 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 580 | +353.1% | -264 to 1,168 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 506 | +321.6% | -199 to 971 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,975,775 | 692,220 | -65.0% | -2,931,026 to 363,915 | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.211 | -2.4% | -0.0268 to 0.0165 | STEADY, no difference beyond the noise |
| host CPU-seconds | 387 | 377 | -2.4% | -47.6 to 29.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.88 | 2.8 | -2.7% | -0.371 to 0.214 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | -1.84 to 8.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 184 | 197 | +6.9% | 10.5 to 14.8 | GAIN |
| throughput (transactions a second) | 197 | 197 | +0.2% | -1.02 to 1.85 | STEADY, no difference beyond the noise |
| queries a second | 3,932 | 3,940 | +0.2% | -20.4 to 36.9 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 11.5 | 6.63 | -42.4% | -5.18 to -4.59 | GAIN |
| latency, 99th percentile (ms) | 16.4 | 8.79 | -46.5% | -10 to -5.22 | GAIN |
| latency, mean (ms) | 6.28 | 4.72 | -24.9% | -3.97 to 0.842 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,032 | +706.3% | 845 to 963 | power given |
| pages holding data, mean (MB) | 121 | 921 | +660.8% | 761 to 839 | power given |
| pages read from disk into the pool (misses) | 1,665,740 | 144,440 | -91.3% | -1,533,022 to -1,509,578 | shown, not judged |
| host CPU busy (share of the run) | 0.301 | 0.255 | -15.1% | -0.0465 to -0.0442 | GAIN |
| host CPU-seconds | 529 | 448 | -15.2% | -82.4 to -78.2 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 6.28 | 4.98 | -20.6% | -1.39 to -1.21 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 5.67 |  | 0.495 to 10.8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,946 | 2,943 | -0.1% | -17.5 to 12 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,954 | 2,953 | -0.1% | -18.7 to 15.5 | STEADY, no difference beyond the noise |
| queries a second | 2,954 | 2,953 | -0.1% | -18.7 to 15.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.342 | 0.336 | -1.8% | -0.0209 to 0.00891 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.473 | 0.478 | +1.2% | -0.0187 to 0.0301 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.204 | 0.199 | -2.6% | -0.0123 to 0.00181 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 508 | +296.8% | -3.71 to 764 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 475 | +292.1% | 3.32 to 705 | power given |
| pages read from disk into the pool (misses) | 1,031,283 | 399,609 | -61.3% | -1,015,347 to -248,000 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.16 | -2.4% | -0.00814 to 0.000197 | STEADY, no difference beyond the noise |
| host CPU-seconds | 289 | 282 | -2.4% | -13.6 to -0.358 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 0.214 | 0.209 | -2.3% | -0.0105 to 0.000538 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.67 |  | -1.2 to 4.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 5.41 | 12.3 | +127.5% | -11.4 to 25.2 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 985 | 986 | +0.1% | -0.974 to 2.54 | STEADY, no difference beyond the noise |
| queries a second | 985 | 986 | +0.1% | -0.974 to 2.54 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.09 | 1.69 | -19.1% | -0.778 to -0.0189 | GAIN |
| latency, 99th percentile (ms) | 3.38 | 3.08 | -9.0% | -1.11 to 0.506 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.14 | 1.04 | -8.2% | -0.247 to 0.0594 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,194 | +833.1% | 1,050 to 1,083 | power given |
| pages holding data, mean (MB) | 119 | 840 | +608.6% | 667 to 775 | power given |
| pages read from disk into the pool (misses) | 418,331 | 108,027 | -74.2% | -340,315 to -280,293 | shown, not judged |
| host CPU busy (share of the run) | 0.263 | 0.231 | -12.3% | -0.0602 to -0.00462 | GAIN |
| host CPU-seconds | 461 | 405 | -12.3% | -104 to -8.85 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 324 | 110 | -66.1% | -842 to 414 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
