# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 8.12 | 5.01 | -38.3% | -10.4 to 4.16 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 984 | +0.1% | -3 to 5.22 | EVEN, no difference beyond the noise |
| queries a second | 983 | 984 | +0.1% | -3 to 5.22 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.87 | 1.96 | +4.8% | -0.269 to 0.449 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.91 | 4.01 | +2.5% | -0.277 to 0.47 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.1 | 1.12 | +1.9% | -0.0942 to 0.135 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 502 | -1.9% | -87 to 67.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 432 | -4.7% | -116 to 73.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,430 | 199,199 | +5.2% | -73,049 to 92,588 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.127 | +5.4% | -0.0418 to 0.0548 | EVEN, no difference beyond the noise |
| host CPU-seconds | 185 | 195 | +5.4% | -64.5 to 84.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 50.4 | 108 | +114.3% | -109 to 224 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.3 |  | -0.964 to 37.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
