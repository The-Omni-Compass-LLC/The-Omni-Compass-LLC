# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.5% | -2.99 to 5.63 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 292 | 293 | +0.4% | -3.3 to 5.49 | STEADY, no difference beyond the noise |
| queries a second | 4,670 | 4,688 | +0.4% | -52.8 to 87.9 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.43 | 4.23 | -4.6% | -0.751 to 0.341 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.24 | 5.74 | -8.0% | -1.3 to 0.295 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.71 | 2.66 | -1.9% | -0.313 to 0.21 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 679 | +32.6% | 22.8 to 311 | power given |
| pages holding data, mean (MB) | 451 | 611 | +35.5% | 26 to 294 | power given |
| pages read from disk into the pool (misses) | 246,820 | 190,658 | -22.8% | -106,981 to -5,343 | shown, not judged |
| host CPU busy (share of the run) | 0.218 | 0.217 | -0.6% | -0.0195 to 0.0169 | STEADY, no difference beyond the noise |
| host CPU-seconds | 133 | 132 | -0.5% | -11.4 to 10.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.95 | 2.93 | -1.0% | -0.242 to 0.185 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.2% | -4.56 to 3.13 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.0% | -1.99 to 2.15 | STEADY, no difference beyond the noise |
| queries a second | 4,697 | 4,699 | +0.0% | -31.9 to 34.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.08 | 3 | -2.3% | -0.353 to 0.209 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.97 | 5.49 | +10.4% | -2.16 to 3.2 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.15 | 2.24 | +4.4% | -0.459 to 0.647 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,050 | +105.1% | 334 to 743 | power given |
| pages holding data, mean (MB) | 464 | 896 | +93.1% | 318 to 545 | power given |
| pages read from disk into the pool (misses) | 655,116 | 132,595 | -79.8% | -574,425 to -470,617 | shown, not judged |
| host CPU busy (share of the run) | 0.177 | 0.171 | -3.0% | -0.0109 to 0.000183 | STEADY, no difference beyond the noise |
| host CPU-seconds | 323 | 314 | -3.0% | -19.9 to 0.406 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.4 | 2.33 | -2.8% | -0.132 to -0.00204 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | -1.57 to 11.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 194 | 194 | -0.1% | -11 to 10.8 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 198 | 197 | -0.3% | -5.58 to 4.31 | STEADY, no difference beyond the noise |
| queries a second | 3,959 | 3,947 | -0.3% | -112 to 86.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.24 | 5.62 | -10.0% | -4.38 to 3.14 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 17.4 | 13.6 | -21.9% | -27.6 to 19.9 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.27 | 2.96 | -9.4% | -0.719 to 0.104 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,076 | +110.1% | 110 to 1,018 | power given |
| pages holding data, mean (MB) | 464 | 907 | +95.5% | 144 to 742 | power given |
| pages read from disk into the pool (misses) | 618,726 | 187,509 | -69.7% | -580,557 to -281,877 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.132 | -6.5% | -0.0386 to 0.0202 | STEADY, no difference beyond the noise |
| host CPU-seconds | 250 | 234 | -6.5% | -68.1 to 35.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.83 | 2.65 | -6.4% | -0.616 to 0.251 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.67 |  | -4.37 to 15.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,961 | 2,962 | +0.0% | -6.61 to 8.92 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,967 | +0.1% | -10.3 to 14.3 | STEADY, no difference beyond the noise |
| queries a second | 2,965 | 2,967 | +0.1% | -10.3 to 14.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.201 | 0.191 | -5.1% | -0.0191 to -0.00161 | GAIN |
| latency, 99th percentile (ms) | 0.338 | 0.34 | +0.6% | -0.00661 to 0.0106 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.154 | 0.175 | +13.6% | 0.0161 to 0.0258 | LOSS |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,168 | +128.2% | 461 to 851 | power given |
| pages holding data, mean (MB) | 466 | 915 | +96.5% | 421 to 477 | power given |
| pages read from disk into the pool (misses) | 368,523 | 81,917 | -77.8% | -296,315 to -276,897 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.107 | -1.3% | -0.00442 to 0.00152 | STEADY, no difference beyond the noise |
| host CPU-seconds | 192 | 189 | -1.3% | -8.15 to 3.03 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.142 | 0.14 | -1.4% | -0.00642 to 0.00249 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | -2.54 to 19.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 4.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2.08 | 2.56 | +22.8% | -1.17 to 2.12 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 981 | 980 | -0.1% | -7.53 to 6.04 | STEADY, no difference beyond the noise |
| queries a second | 981 | 980 | -0.1% | -7.53 to 6.04 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.91 | 1.86 | -3.0% | -0.726 to 0.611 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.41 | 5.11 | +15.8% | -2.84 to 4.23 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.24 | 1.24 | +0.5% | -0.262 to 0.274 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.5% | 704 to 745 | power given |
| pages holding data, mean (MB) | 455 | 890 | +95.6% | 409 to 461 | power given |
| pages read from disk into the pool (misses) | 192,597 | 70,172 | -63.6% | -124,997 to -119,852 | shown, not judged |
| host CPU busy (share of the run) | 0.17 | 0.166 | -2.5% | -0.0226 to 0.014 | STEADY, no difference beyond the noise |
| host CPU-seconds | 307 | 299 | -2.5% | -40.1 to 24.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 333 | 295 | -11.3% | -226 to 151 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
