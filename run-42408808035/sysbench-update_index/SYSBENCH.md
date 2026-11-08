# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 5.1 | 6.65 | +30.5% | -0.494 to 3.61 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 984 | 983 | -0.1% | -1.23 to -0.771 | LOSS |
| queries a second | 984 | 983 | -0.1% | -1.23 to -0.771 | LOSS |
| latency, 95th percentile (ms) | 2.04 | 1.96 | -3.9% | -0.498 to 0.34 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.74 | 8.86 | +1.4% | -1.12 to 1.37 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.23 | 1.22 | -1.3% | -0.105 to 0.072 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,235 | +141.3% | 702 to 745 | power given |
| pages holding data, mean (MB) | 458 | 888 | +94.0% | 407 to 453 | power given |
| pages read from disk into the pool (misses) | 190,940 | 71,436 | -62.6% | -125,952 to -113,056 | shown, not judged |
| host CPU busy (share of the run) | 0.233 | 0.227 | -2.6% | -0.0347 to 0.0225 | STEADY, no difference beyond the noise |
| host CPU-seconds | 408 | 397 | -2.6% | -60 to 38.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 179 | 134 | -25.4% | -119 to 28.2 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
