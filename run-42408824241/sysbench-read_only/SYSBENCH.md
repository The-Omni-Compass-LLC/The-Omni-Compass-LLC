# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | +0.0% | -5.67 to 5.78 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.1% | -5.24 to 5.8 | STEADY, no difference beyond the noise |
| queries a second | 4,701 | 4,705 | +0.1% | -83.8 to 92.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.04 | 3.21 | +5.6% | -0.212 to 0.551 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.1 | 4.41 | +7.6% | -0.217 to 0.837 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.37 | 2.41 | +1.6% | -0.0701 to 0.146 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 494 | +286.0% | 329 to 404 | power given |
| pages holding data, mean (MB) | 120 | 454 | +278.5% | 320 to 349 | power given |
| pages read from disk into the pool (misses) | 1,981,006 | 685,864 | -65.4% | -1,491,150 to -1,099,136 | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.198 | +1.0% | -0.0083 to 0.0121 | STEADY, no difference beyond the noise |
| host CPU-seconds | 357 | 361 | +1.0% | -15.1 to 22.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.65 | 2.67 | +0.9% | -0.0931 to 0.142 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 2.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
