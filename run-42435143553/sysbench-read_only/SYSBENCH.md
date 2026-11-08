# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | +0.1% | -1.87 to 2.55 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.1% | -1.62 to 2.1 | STEADY, no difference beyond the noise |
| queries a second | 4,715 | 4,718 | +0.1% | -26 to 33.6 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.39 | 2.36 | -1.2% | -0.0882 to 0.0322 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.7 | 3.64 | -1.8% | -0.0678 to -0.0649 | GAIN |
| latency, mean (ms) | 1.75 | 1.74 | -0.9% | -0.0443 to 0.0125 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 462 | 458 | -0.7% | -17.4 to 11 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 656,806 | 656,665 | -0.0% | -13,098 to 12,816 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.147 | -0.4% | -0.00368 to 0.0026 | STEADY, no difference beyond the noise |
| host CPU-seconds | 269 | 268 | -0.4% | -7.09 to 5.07 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.99 | 1.98 | -0.5% | -0.0453 to 0.0261 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
