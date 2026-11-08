# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.3% | -7.52 to 9.06 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 293 | 294 | +0.2% | -5.69 to 6.95 | STEADY, no difference beyond the noise |
| queries a second | 4,686 | 4,696 | +0.2% | -91 to 111 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.95 | 4.86 | -1.9% | -0.527 to 0.342 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.22 | 7.05 | -2.4% | -1.54 to 1.19 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.14 | 3.08 | -1.8% | -0.0899 to -0.0208 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 813 | +58.8% | 44.6 to 558 | power given |
| pages holding data, mean (MB) | 454 | 734 | +61.8% | 58.7 to 502 | power given |
| pages read from disk into the pool (misses) | 246,186 | 152,141 | -38.2% | -171,240 to -16,850 | shown, not judged |
| host CPU busy (share of the run) | 0.241 | 0.239 | -0.7% | -0.00933 to 0.00586 | STEADY, no difference beyond the noise |
| host CPU-seconds | 143 | 142 | -0.6% | -5.19 to 3.41 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.21 | 3.18 | -1.0% | -0.0603 to -0.00091 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 294 | -0.6% | -3.42 to -0.302 | LOSS |
| throughput (transactions a second) | 296 | 294 | -0.7% | -3.44 to -0.458 | LOSS |
| queries a second | 4,740 | 4,709 | -0.7% | -55 to -7.33 | LOSS |
| latency, 95th percentile (ms) | 4.28 | 4.2 | -1.8% | -0.266 to 0.114 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.84 | 5.64 | -3.5% | -0.463 to 0.0492 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.18 | 3.12 | -1.8% | -0.113 to -0.000443 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 815 | +59.2% | 206 to 400 | power given |
| pages holding data, mean (MB) | 463 | 732 | +58.0% | 194 to 343 | power given |
| pages read from disk into the pool (misses) | 659,424 | 234,821 | -64.4% | -503,144 to -346,062 | shown, not judged |
| host CPU busy (share of the run) | 0.251 | 0.246 | -2.0% | -0.00974 to -0.000134 | GAIN |
| host CPU-seconds | 446 | 438 | -1.9% | -17 to -0.312 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.29 | 3.25 | -1.3% | -0.0995 to 0.0127 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191 | 194 | +1.6% | 1.76 to 4.2 | GAIN |
| throughput (transactions a second) | 196 | 195 | -0.4% | -1.24 to -0.277 | LOSS |
| queries a second | 3,912 | 3,897 | -0.4% | -24.8 to -5.54 | LOSS |
| latency, 95th percentile (ms) | 8.58 | 6.28 | -26.8% | -3.22 to -1.39 | GAIN |
| latency, 99th percentile (ms) | 13.8 | 9.28 | -32.7% | -6.48 to -2.55 | GAIN |
| latency, mean (ms) | 4.43 | 3.92 | -11.4% | -0.909 to -0.1 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,042 | +103.5% | 508 to 552 | power given |
| pages holding data, mean (MB) | 462 | 930 | +101.3% | 445 to 491 | power given |
| pages read from disk into the pool (misses) | 620,959 | 119,892 | -80.7% | -535,107 to -467,026 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.182 | -5.6% | -0.0128 to -0.00873 | GAIN |
| host CPU-seconds | 357 | 337 | -5.5% | -23.6 to -16 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.06 | 3.77 | -7.0% | -0.324 to -0.244 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 4.67 |  | 3.23 to 6.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,948 | 2,945 | -0.1% | -14.7 to 9.95 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,954 | 2,953 | -0.1% | -11.3 to 7.58 | STEADY, no difference beyond the noise |
| queries a second | 2,954 | 2,953 | -0.1% | -11.3 to 7.58 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.303 | 0.305 | +0.5% | -0.0266 to 0.0299 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.448 | 0.451 | +0.6% | -0.0387 to 0.044 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.189 | 0.193 | +2.0% | -0.0133 to 0.021 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 569 | +11.1% | -187 to 300 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 514 | +10.7% | -155 to 254 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,243 | 324,036 | -12.0% | -236,906 to 148,492 | shown, not judged |
| host CPU busy (share of the run) | 0.152 | 0.155 | +1.8% | -0.00907 to 0.0147 | STEADY, no difference beyond the noise |
| host CPU-seconds | 268 | 273 | +1.8% | -16.1 to 25.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.199 | 0.203 | +1.9% | -0.0125 to 0.02 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 243 | 271 | +11.6% | -17.9 to 74.2 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 988 | 988 | +0.0% | -4.54 to 4.73 | STEADY, no difference beyond the noise |
| queries a second | 988 | 988 | +0.0% | -4.54 to 4.73 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.84 | 2.81 | -0.8% | -1.35 to 1.31 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.64 | 5.92 | -10.9% | -5.47 to 4.02 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.03 | 0.993 | -3.3% | -0.303 to 0.236 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,235 | +141.3% | 702 to 745 | power given |
| pages holding data, mean (MB) | 455 | 887 | +95.0% | 404 to 460 | power given |
| pages read from disk into the pool (misses) | 192,214 | 71,446 | -62.8% | -129,448 to -112,087 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.112 | -4.7% | -0.0194 to 0.00819 | STEADY, no difference beyond the noise |
| host CPU-seconds | 208 | 198 | -4.7% | -33.8 to 14.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.91 | 1.62 | -15.0% | -0.849 to 0.277 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
