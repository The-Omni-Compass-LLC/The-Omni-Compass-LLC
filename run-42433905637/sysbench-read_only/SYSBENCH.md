# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 297 | +0.1% | -1.73 to 2.53 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 297 | +0.1% | -1.71 to 2.38 | STEADY, no difference beyond the noise |
| queries a second | 4,744 | 4,750 | +0.1% | -27.4 to 38 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.17 | 1.94 | -10.6% | -0.652 to 0.193 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.23 | 3.98 | -5.8% | -0.345 to -0.147 | GAIN |
| latency, mean (ms) | 1.31 | 1.27 | -3.0% | -0.243 to 0.165 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 462 | 458 | -0.7% | -16.1 to 9.98 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,418 | 655,951 | +0.1% | -3,539 to 4,604 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.103 | -2.1% | -0.02 to 0.0155 | STEADY, no difference beyond the noise |
| host CPU-seconds | 189 | 185 | -2.1% | -35.9 to 28 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.4 | 1.37 | -2.2% | -0.269 to 0.207 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
