# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `dca8d09bbaa4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 296 | +0.7% | -3.44 to 7.27 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 296 | +0.7% | -3 to 6.97 | STEADY, no difference beyond the noise |
| queries a second | 4,709 | 4,741 | +0.7% | -48 to 112 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.86 | 2.9 | +1.2% | -0.0396 to 0.108 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.38 | 4.49 | +2.4% | -0.12 to 0.329 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.38 | +1.9% | -0.0711 to 0.123 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 486 | +279.5% | -110 to 826 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 456 | +278.2% | -102 to 772 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 584,177 | 311,716 | -46.6% | -456,021 to -88,901 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.103 | +1.7% | -0.00261 to 0.00601 | STEADY, no difference beyond the noise |
| host CPU-seconds | 60.6 | 61.6 | +1.7% | -1.58 to 3.63 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.35 | 1.37 | +1.0% | -0.0238 to 0.0512 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.33 |  | -0.101 to 2.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `dca8d09bbaa4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 297 | +0.4% | -2.27 to 4.4 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.3% | -2.25 to 4.09 | STEADY, no difference beyond the noise |
| queries a second | 4,741 | 4,756 | +0.3% | -36 to 65.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.74 | 1.85 | +6.2% | -0.0609 to 0.277 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.73 | 3.82 | +2.4% | -0.447 to 0.624 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.24 | 1.25 | +0.7% | -0.0579 to 0.0763 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 128 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 120 | 120 | -0.0% | -0.19 to 0.12 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,984,578 | 1,985,820 | +0.1% | -13,458 to 15,941 | shown, not judged |
| host CPU busy (share of the run) | 0.0969 | 0.0999 | +3.2% | -0.000412 to 0.00653 | STEADY, no difference beyond the noise |
| host CPU-seconds | 174 | 180 | +3.2% | -0.784 to 11.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.29 | 1.33 | +2.8% | 0.00325 to 0.068 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `dca8d09bbaa4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 178 | 194 | +8.6% | 14.9 to 15.9 | GAIN |
| throughput (transactions a second) | 196 | 196 | +0.1% | -0.576 to 0.842 | STEADY, no difference beyond the noise |
| queries a second | 3,923 | 3,926 | +0.1% | -11.5 to 16.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 13 | 7.52 | -42.1% | -5.77 to -5.15 | GAIN |
| latency, 99th percentile (ms) | 18.4 | 11.5 | -37.4% | -7.24 to -6.5 | GAIN |
| latency, mean (ms) | 6.22 | 5.09 | -18.2% | -1.17 to -1.09 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,054 | +723.1% | 873 to 978 | power given |
| pages holding data, mean (MB) | 119 | 940 | +691.0% | 768 to 875 | power given |
| pages read from disk into the pool (misses) | 1,662,813 | 137,935 | -91.7% | -1,660,640 to -1,389,115 | shown, not judged |
| host CPU busy (share of the run) | 0.309 | 0.263 | -14.9% | -0.0548 to -0.0373 | GAIN |
| host CPU-seconds | 544 | 462 | -15.0% | -96.9 to -66.2 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 6.66 | 5.21 | -21.7% | -1.62 to -1.27 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 5.23 to 8.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `dca8d09bbaa4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,956 | 2,964 | +0.3% | -10.9 to 26.3 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,963 | 2,970 | +0.2% | -9.11 to 23.1 | STEADY, no difference beyond the noise |
| queries a second | 2,963 | 2,970 | +0.2% | -9.11 to 23.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.198 | 0.175 | -11.9% | -0.103 to 0.0557 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.318 | 0.309 | -2.7% | -0.0718 to 0.0544 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0933 | 0.0948 | +1.6% | -0.035 to 0.0379 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 311 | +142.8% | -211 to 577 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 287 | +136.7% | -193 to 524 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,029,110 | 725,647 | -29.5% | -975,197 to 368,272 | shown, not judged |
| host CPU busy (share of the run) | 0.0738 | 0.0757 | +2.7% | -0.0302 to 0.0342 | STEADY, no difference beyond the noise |
| host CPU-seconds | 132 | 135 | +2.7% | -53.8 to 60.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0978 | 0.1 | +2.4% | -0.0406 to 0.0453 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.33 |  | -2.46 to 5.13 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `dca8d09bbaa4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 13.9 | 20.4 | +46.9% | 2.88 to 10.1 | GAIN |
| throughput (transactions a second) | 983 | 984 | +0.2% | -2.35 to 5.48 | STEADY, no difference beyond the noise |
| queries a second | 983 | 984 | +0.2% | -2.35 to 5.48 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.19 | 1.73 | -20.9% | -0.669 to -0.247 | GAIN |
| latency, 99th percentile (ms) | 4.08 | 3.91 | -4.2% | -0.605 to 0.262 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.13 | 1.05 | -7.0% | -0.162 to 0.00292 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,247 | +874.5% | 985 to 1,254 | power given |
| pages holding data, mean (MB) | 119 | 856 | +617.2% | 674 to 798 | power given |
| pages read from disk into the pool (misses) | 416,859 | 92,403 | -77.8% | -383,392 to -265,521 | shown, not judged |
| host CPU busy (share of the run) | 0.247 | 0.218 | -11.9% | -0.0542 to -0.00452 | GAIN |
| host CPU-seconds | 434 | 382 | -11.9% | -95 to -8.17 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 70.6 | 41.2 | -41.6% | -66.1 to 7.4 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
