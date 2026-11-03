# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 15.3 | 18.1 | +18.4% | -3.1 to 8.74 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 984 | 983 | -0.1% | -2.79 to 1.04 | STEADY, no difference beyond the noise |
| queries a second | 984 | 983 | -0.1% | -2.79 to 1.04 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.34 | 2.39 | +2.3% | -0.21 to 0.318 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.74 | 9.39 | +7.5% | 0.205 to 1.11 | LOSS |
| latency, mean (ms) | 1.27 | 1.28 | +0.7% | -0.0803 to 0.0977 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.5% | 705 to 744 | power given |
| pages holding data, mean (MB) | 460 | 889 | +93.3% | 414 to 444 | power given |
| pages read from disk into the pool (misses) | 186,286 | 71,808 | -61.5% | -131,590 to -97,365 | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.206 | -3.1% | -0.0349 to 0.0219 | STEADY, no difference beyond the noise |
| host CPU-seconds | 373 | 362 | -3.0% | -61.1 to 38.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 56.2 | 43.8 | -22.0% | -49.8 to 25.1 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
