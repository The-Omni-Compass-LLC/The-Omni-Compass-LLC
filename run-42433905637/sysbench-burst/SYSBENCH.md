# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 282 | 283 | +0.4% | -19.4 to 21.5 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.6% | -10.9 to 7.34 | STEADY, no difference beyond the noise |
| queries a second | 4,759 | 4,730 | -0.6% | -175 to 117 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 14 | 6.97 | -50.0% | -43.2 to 29.2 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 305 | 252 | -17.3% | -183 to 77.5 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 10.5 | 8.18 | -22.0% | -7.69 to 3.08 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,260 | +146.2% | 606 to 891 | power given |
| pages holding data, mean (MB) | 453 | 974 | +114.9% | 466 to 575 | power given |
| pages read from disk into the pool (misses) | 243,848 | 81,377 | -66.6% | -172,799 to -152,142 | shown, not judged |
| host CPU busy (share of the run) | 0.17 | 0.164 | -3.5% | -0.0131 to 0.00104 | STEADY, no difference beyond the noise |
| host CPU-seconds | 102 | 98.2 | -3.6% | -7.75 to 0.468 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.37 | 2.28 | -3.9% | -0.308 to 0.123 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.67 |  | -0.585 to 11.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
