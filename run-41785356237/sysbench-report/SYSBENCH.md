# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 297 | 295 | -0.6% | -8.07 to 4.61 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 295 | -0.5% | -8.42 to 5.15 | STEADY, no difference beyond the noise |
| queries a second | 4,750 | 4,724 | -0.5% | -135 to 82.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.92 | 3.18 | +9.1% | -0.539 to 1.07 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.49 | 4.87 | +8.5% | -0.743 to 1.5 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.41 | 1.45 | +3.1% | -0.296 to 0.382 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 398 | +210.8% | 124 to 416 | power given |
| pages holding data, mean (MB) | 120 | 373 | +209.8% | 114 to 391 | power given |
| pages read from disk into the pool (misses) | 592,106 | 332,610 | -43.8% | -260,828 to -258,165 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.108 | +3.2% | -0.0212 to 0.0278 | STEADY, no difference beyond the noise |
| host CPU-seconds | 63.1 | 65 | +3.1% | -12.6 to 16.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.4 | 1.45 | +3.7% | -0.257 to 0.36 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 290 | -0.2% | -3.46 to 2.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | +0.3% | 0.154 to 1.64 | GAIN |
| queries a second | 4,729 | 4,743 | +0.3% | 2.47 to 26.3 | GAIN |
| latency, 95th percentile (ms) | 3.06 | 2.85 | -6.9% | -0.343 to -0.0818 | GAIN |
| latency, 99th percentile (ms) | 53.5 | 66.5 | +24.2% | -70.7 to 96.6 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.74 | 3.92 | +4.9% | -1.54 to 1.91 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,204 | +840.8% | 1,016 to 1,137 | power given |
| pages holding data, mean (MB) | 120 | 956 | +694.3% | 825 to 847 | power given |
| pages read from disk into the pool (misses) | 2,006,240 | 81,753 | -95.9% | -2,003,760 to -1,845,214 | shown, not judged |
| host CPU busy (share of the run) | 0.168 | 0.154 | -7.9% | -0.0176 to -0.00899 | GAIN |
| host CPU-seconds | 300 | 276 | -7.9% | -31.6 to -15.7 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.27 | 2.1 | -7.7% | -0.211 to -0.137 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 19 |  | 16.5 to 21.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 11.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 184 | 197 | +7.0% | 11.1 to 14.5 | GAIN |
| throughput (transactions a second) | 197 | 197 | +0.4% | -0.309 to 2.07 | STEADY, no difference beyond the noise |
| queries a second | 3,931 | 3,949 | +0.4% | -6.18 to 41.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 11.5 | 6.96 | -39.6% | -5.09 to -4.04 | GAIN |
| latency, 99th percentile (ms) | 16 | 9.22 | -42.4% | -7.42 to -6.17 | GAIN |
| latency, mean (ms) | 5.84 | 4.91 | -16.0% | -1.03 to -0.836 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 949 | +641.8% | 737 to 906 | power given |
| pages holding data, mean (MB) | 120 | 857 | +612.8% | 645 to 829 | power given |
| pages read from disk into the pool (misses) | 1,665,728 | 213,577 | -87.2% | -1,515,429 to -1,388,872 | shown, not judged |
| host CPU busy (share of the run) | 0.309 | 0.268 | -13.1% | -0.0492 to -0.0317 | GAIN |
| host CPU-seconds | 543 | 472 | -13.2% | -86.7 to -56.4 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 6.45 | 5.24 | -18.8% | -1.45 to -0.977 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 4.52 to 9.48 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,947 | 2,946 | -0.0% | -9.1 to 7.69 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,951 | -0.0% | -10.4 to 8.42 | STEADY, no difference beyond the noise |
| queries a second | 2,952 | 2,951 | -0.0% | -10.4 to 8.42 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.336 | 0.328 | -2.4% | -0.0252 to 0.00921 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.443 | 0.44 | -0.6% | -0.0141 to 0.00881 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.193 | -3.7% | -0.0128 to -0.00188 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 326 | +155.0% | 27.7 to 369 | power given |
| pages holding data, mean (MB) | 121 | 311 | +156.5% | 31.2 to 348 | power given |
| pages read from disk into the pool (misses) | 1,029,648 | 617,501 | -40.0% | -696,810 to -127,483 | shown, not judged |
| host CPU busy (share of the run) | 0.161 | 0.157 | -2.9% | -0.00935 to 5.06e-05 | STEADY, no difference beyond the noise |
| host CPU-seconds | 284 | 276 | -2.8% | -16.7 to 0.63 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.211 | 0.205 | -2.8% | -0.0129 to 0.00107 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3.66 | 5.99 | +63.5% | -1.57 to 6.22 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 983 | 984 | +0.2% | -0.265 to 3.22 | STEADY, no difference beyond the noise |
| queries a second | 983 | 984 | +0.2% | -0.265 to 3.22 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.28 | 1.88 | -17.5% | -0.619 to -0.179 | GAIN |
| latency, 99th percentile (ms) | 4.2 | 3.93 | -6.4% | -0.551 to 0.0123 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 1.1 | -7.6% | -0.209 to 0.0256 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,248 | +874.8% | 991 to 1,248 | power given |
| pages holding data, mean (MB) | 118 | 856 | +623.2% | 684 to 791 | power given |
| pages read from disk into the pool (misses) | 416,868 | 93,149 | -77.7% | -391,345 to -256,093 | shown, not judged |
| host CPU busy (share of the run) | 0.266 | 0.238 | -10.7% | -0.0577 to 0.000781 | STEADY, no difference beyond the noise |
| host CPU-seconds | 467 | 417 | -10.6% | -99.9 to 0.731 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 280 | 157 | -43.9% | -281 to 35.7 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
