# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
