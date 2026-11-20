# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7.74 | 2.09 | -73.1% | -38.1 to 26.8 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 974 | 980 | +0.6% | -19.6 to 31.4 | STEADY, no difference beyond the noise |
| queries a second | 974 | 980 | +0.6% | -19.6 to 31.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.51 | 2.76 | -21.2% | -2.11 to 0.621 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 831 | 22.2 | -97.3% | -4,288 to 2,672 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 23.5 | 1.8 | -92.3% | -114 to 71 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,255 | +880.1% | 1,028 to 1,225 | power given |
| pages holding data, mean (MB) | 119 | 864 | +627.8% | 713 to 777 | power given |
| pages read from disk into the pool (misses) | 416,190 | 88,010 | -78.9% | -365,480 to -290,880 | shown, not judged |
| host CPU busy (share of the run) | 0.29 | 0.272 | -6.2% | -0.075 to 0.0393 | STEADY, no difference beyond the noise |
| host CPU-seconds | 507 | 477 | -6.0% | -131 to 70.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1,393 | 548 | -60.7% | -4,553 to 2,864 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
