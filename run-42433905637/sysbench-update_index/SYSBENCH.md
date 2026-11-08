# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 147 | 144 | -2.0% | -79.6 to 73.9 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 987 | 988 | +0.2% | -2.32 to 5.52 | STEADY, no difference beyond the noise |
| queries a second | 987 | 988 | +0.2% | -2.32 to 5.52 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 12.6 | 56.4 | +348.7% | -18.9 to 107 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 71.2 | 172 | +141.1% | 44.6 to 156 | LOSS |
| latency, mean (ms) | 4.02 | 9.87 | +145.6% | 1.21 to 10.5 | LOSS |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,213 | +136.8% | 647 to 754 | power given |
| pages holding data, mean (MB) | 456 | 892 | +95.8% | 403 to 470 | power given |
| pages read from disk into the pool (misses) | 192,764 | 69,538 | -63.9% | -137,786 to -108,665 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.136 | -4.5% | -0.0263 to 0.0135 | STEADY, no difference beyond the noise |
| host CPU-seconds | 249 | 238 | -4.3% | -45.5 to 24.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.96 | 3.65 | -7.8% | -3.44 to 2.82 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
