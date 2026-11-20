# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 280 | 279 | -0.5% | -9.41 to 6.58 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.2% | -8.53 to 7.2 | STEADY, no difference beyond the noise |
| queries a second | 4,724 | 4,714 | -0.2% | -136 to 115 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 17.5 | 11.6 | -33.8% | -48.2 to 36.4 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 214 | 127 | -40.9% | -363 to 188 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 8.36 | 5.86 | -29.9% | -11.6 to 6.57 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,172 | +815.5% | 1,023 to 1,065 | power given |
| pages holding data, mean (MB) | 121 | 924 | +666.7% | 778 to 829 | power given |
| pages read from disk into the pool (misses) | 590,860 | 83,154 | -85.9% | -570,462 to -444,951 | shown, not judged |
| host CPU busy (share of the run) | 0.168 | 0.159 | -5.5% | -0.0116 to -0.00692 | GAIN |
| host CPU-seconds | 101 | 95 | -5.5% | -7.07 to -4.05 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.36 | 2.24 | -5.0% | -0.182 to -0.0554 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | 5 to 5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.5% | -7.49 to 10.5 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.0% | -5.07 to 5.25 | STEADY, no difference beyond the noise |
| queries a second | 4,693 | 4,694 | +0.0% | -81.1 to 84 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.93 | 2.88 | -1.9% | -0.409 to 0.298 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 122 | 4.49 | -96.3% | -622 to 388 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 4.53 | 2.07 | -54.4% | -13.1 to 8.19 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 537 | +319.9% | 222 to 597 | power given |
| pages holding data, mean (MB) | 120 | 488 | +307.4% | 219 to 518 | power given |
| pages read from disk into the pool (misses) | 1,973,915 | 611,274 | -69.0% | -1,697,671 to -1,027,611 | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.173 | -0.1% | -0.00583 to 0.00554 | STEADY, no difference beyond the noise |
| host CPU-seconds | 317 | 316 | -0.1% | -10.9 to 10.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.36 | 2.35 | -0.6% | -0.149 to 0.119 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | -1.84 to 8.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195 | 196 | +0.8% | -3.32 to 6.46 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 198 | 198 | +0.1% | -3.14 to 3.41 | STEADY, no difference beyond the noise |
| queries a second | 3,954 | 3,957 | +0.1% | -62.8 to 68.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.98 | 6 | -14.0% | -2.84 to 0.885 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.8 | 10.3 | -19.2% | -6.95 to 2.02 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.24 | 2.97 | -8.5% | -1.04 to 0.485 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,079 | +743.3% | 939 to 964 | power given |
| pages holding data, mean (MB) | 121 | 932 | +667.5% | 749 to 872 | power given |
| pages read from disk into the pool (misses) | 1,668,820 | 221,301 | -86.7% | -1,666,126 to -1,228,910 | shown, not judged |
| host CPU busy (share of the run) | 0.151 | 0.13 | -14.2% | -0.0346 to -0.00839 | GAIN |
| host CPU-seconds | 268 | 230 | -14.2% | -61.4 to -14.7 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.03 | 2.58 | -14.9% | -0.737 to -0.164 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 7.67 |  | 0.495 to 14.8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,928 | 2,928 | +0.0% | -7.7 to 8.74 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,932 | 2,932 | +0.0% | -6.34 to 8.05 | STEADY, no difference beyond the noise |
| queries a second | 2,932 | 2,932 | +0.0% | -6.34 to 8.05 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.23 | 0.225 | -2.3% | -0.0303 to 0.0197 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.414 | 0.414 | +0.1% | -0.0183 to 0.019 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.144 | 0.139 | -3.4% | -0.00832 to -0.00137 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 593 | +363.5% | -64.8 to 995 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 547 | +351.4% | -33 to 885 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,029,474 | 396,944 | -61.4% | -1,000,674 to -264,386 | shown, not judged |
| host CPU busy (share of the run) | 0.128 | 0.126 | -1.5% | -0.0106 to 0.00692 | STEADY, no difference beyond the noise |
| host CPU-seconds | 237 | 234 | -1.4% | -19.8 to 13 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.176 | 0.174 | -1.5% | -0.0149 to 0.00976 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 4.56 | 7.41 | +62.5% | -0.841 to 6.54 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 984 | 984 | -0.0% | -4.25 to 3.78 | STEADY, no difference beyond the noise |
| queries a second | 984 | 984 | -0.0% | -4.25 to 3.78 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.01 | 1.65 | -18.0% | -0.563 to -0.163 | GAIN |
| latency, 99th percentile (ms) | 3.15 | 2.7 | -14.5% | -0.823 to -0.0928 | GAIN |
| latency, mean (ms) | 1.12 | 1.04 | -7.5% | -0.177 to 0.00854 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,268 | +890.5% | 1,081 to 1,199 | power given |
| pages holding data, mean (MB) | 118 | 867 | +633.2% | 731 to 766 | power given |
| pages read from disk into the pool (misses) | 418,801 | 84,124 | -79.9% | -370,317 to -299,037 | shown, not judged |
| host CPU busy (share of the run) | 0.257 | 0.235 | -8.8% | -0.0481 to 0.00258 | STEADY, no difference beyond the noise |
| host CPU-seconds | 445 | 408 | -8.4% | -77.5 to 2.39 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 228 | 120 | -47.2% | -277 to 61.8 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
