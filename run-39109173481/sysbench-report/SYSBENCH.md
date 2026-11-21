# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.3% | -4.82 to 2.99 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 293 | -0.3% | -4.17 to 2.36 | EVEN, no difference beyond the noise |
| queries a second | 4,707 | 4,692 | -0.3% | -66.7 to 37.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.44 | 5.47 | +0.6% | -0.532 to 0.601 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.3 | 7.26 | -0.6% | -0.792 to 0.707 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.54 | 3.52 | -0.6% | -0.372 to 0.328 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 143 | +11.5% | 13.6 to 15.8 | power given |
| pages holding data, mean (MB) | 121 | 141 | +16.6% | 10.9 to 29.3 | power given |
| pages read from disk into the pool (misses) | 593,558 | 541,827 | -8.7% | -128,249 to 24,788 | shown, not judged |
| host CPU busy (share of the run) | 0.217 | 0.214 | -1.3% | -0.0354 to 0.03 | EVEN, no difference beyond the noise |
| host CPU-seconds | 121 | 119 | -1.3% | -20.8 to 17.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.68 | 2.66 | -1.0% | -0.489 to 0.436 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | +0.1% | -4.27 to 4.81 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.1% | -3.96 to 4.43 | EVEN, no difference beyond the noise |
| queries a second | 4,716 | 4,720 | +0.1% | -63.3 to 71 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.41 | 4.43 | +0.6% | -0.0881 to 0.141 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.47 | 6.55 | +1.2% | -0.368 to 0.525 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.36 | 3.36 | -0.2% | -0.0499 to 0.0373 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 139 | +8.4% | 3.16 to 18.4 | power given |
| pages holding data, mean (MB) | 120 | 136 | +13.2% | 12.7 to 19.1 | power given |
| pages read from disk into the pool (misses) | 1,978,276 | 1,882,194 | -4.9% | -234,866 to 42,702 | shown, not judged |
| host CPU busy (share of the run) | 0.208 | 0.207 | -0.2% | -0.0037 to 0.00278 | EVEN, no difference beyond the noise |
| host CPU-seconds | 346 | 345 | -0.3% | -6.54 to 4.55 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.57 | 2.56 | -0.4% | -0.0277 to 0.00816 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.67 |  | 6.23 to 9.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 163 | 153 | -6.1% | -34 to 14.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 198 | +0.1% | -1.82 to 2.03 | EVEN, no difference beyond the noise |
| queries a second | 3,955 | 3,957 | +0.1% | -36.4 to 40.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 98.6 | 153 | +55.0% | -90.3 to 199 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 300 | 401 | +33.4% | -198 to 399 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 20.2 | 28.8 | +42.4% | -16.5 to 33.6 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 141 | +10.3% | 10.6 to 15.9 | power given |
| pages holding data, mean (MB) | 121 | 133 | +9.8% | 10.3 to 13.5 | power given |
| pages read from disk into the pool (misses) | 1,671,492 | 1,599,255 | -4.3% | -149,745 to 5,271 | shown, not judged |
| host CPU busy (share of the run) | 0.211 | 0.211 | -0.1% | -0.00635 to 0.00607 | EVEN, no difference beyond the noise |
| host CPU-seconds | 374 | 374 | +0.0% | -9.76 to 9.84 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.05 | 5.39 | +6.7% | -0.374 to 1.05 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9.33 |  | 6.46 to 12.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,961 | 2,963 | +0.1% | -6.67 to 10.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,967 | +0.1% | -4.1 to 8.12 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,967 | +0.1% | -4.1 to 8.12 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.18 | 0.149 | -17.4% | -0.0717 to 0.00906 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.312 | 0.305 | -2.3% | -0.0422 to 0.0276 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0918 | 0.0871 | -5.1% | -0.0283 to 0.0189 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 134 | +4.9% | -2.04 to 14.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 130 | +7.5% | 4.11 to 14 | power given |
| pages read from disk into the pool (misses) | 1,029,126 | 1,007,664 | -2.1% | -50,360 to 7,435 | shown, not judged |
| host CPU busy (share of the run) | 0.0719 | 0.0668 | -7.1% | -0.0157 to 0.00553 | EVEN, no difference beyond the noise |
| host CPU-seconds | 129 | 120 | -7.1% | -28.2 to 9.96 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0957 | 0.0889 | -7.1% | -0.021 to 0.00738 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.67 |  | -1.07 to 10.4 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2.03 | 1.95 | -3.6% | -3.66 to 3.52 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 983 | -0.1% | -5.03 to 3.76 | EVEN, no difference beyond the noise |
| queries a second | 983 | 983 | -0.1% | -5.03 to 3.76 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.39 | 2.53 | +6.0% | -0.453 to 0.741 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.11 | 4.34 | +5.6% | -1.1 to 1.56 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.26 | 1.28 | +2.2% | -0.151 to 0.205 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 146 | +13.9% | 13.3 to 22.3 | power given |
| pages holding data, mean (MB) | 118 | 129 | +9.2% | 7.23 to 14.6 | power given |
| pages read from disk into the pool (misses) | 415,718 | 402,508 | -3.2% | -18,874 to -7,547 | shown, not judged |
| host CPU busy (share of the run) | 0.211 | 0.317 | +50.8% | -0.0427 to 0.256 | EVEN, no difference beyond the noise |
| host CPU-seconds | 326 | 494 | +51.7% | -63.4 to 400 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 408 | 712 | +74.5% | -1,033 to 1,641 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
