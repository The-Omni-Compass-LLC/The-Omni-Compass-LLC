# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 10.7 | 13.4 | +25.6% | -2.97 to 8.43 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 984 | 983 | -0.1% | -5.46 to 3.7 | STEADY, no difference beyond the noise |
| queries a second | 984 | 983 | -0.1% | -5.46 to 3.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.85 | 1.75 | -5.5% | -0.498 to 0.293 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.85 | 5.79 | -1.0% | -0.916 to 0.796 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.15 | 1.13 | -2.0% | -0.134 to 0.087 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.4% | 702 to 746 | power given |
| pages holding data, mean (MB) | 460 | 888 | +93.1% | 413 to 443 | power given |
| pages read from disk into the pool (misses) | 186,090 | 71,492 | -61.6% | -136,558 to -92,638 | shown, not judged |
| host CPU busy (share of the run) | 0.23 | 0.223 | -3.1% | -0.0379 to 0.0238 | STEADY, no difference beyond the noise |
| host CPU-seconds | 404 | 392 | -3.0% | -65.6 to 41.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 87.2 | 64.6 | -25.9% | -89 to 43.8 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
