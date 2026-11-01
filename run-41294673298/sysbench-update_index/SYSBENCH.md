# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 9.26 | 14.9 | +61.4% | -8.54 to 19.9 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 985 | 984 | -0.1% | -8.15 to 6.92 | STEADY, no difference beyond the noise |
| queries a second | 985 | 984 | -0.1% | -8.15 to 6.92 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.72 | 1.67 | -3.2% | -0.288 to 0.179 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.15 | 3.49 | +10.8% | -0.521 to 1.2 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 1.27 | +21.1% | -0.787 to 1.23 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.4% | 704 to 744 | power given |
| pages holding data, mean (MB) | 457 | 888 | +94.6% | 409 to 455 | power given |
| pages read from disk into the pool (misses) | 191,050 | 71,535 | -62.6% | -131,947 to -107,084 | shown, not judged |
| host CPU busy (share of the run) | 0.23 | 0.221 | -4.2% | -0.0339 to 0.0143 | STEADY, no difference beyond the noise |
| host CPU-seconds | 404 | 387 | -4.2% | -58.7 to 24.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 99.8 | 69.3 | -30.5% | -109 to 48.4 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
