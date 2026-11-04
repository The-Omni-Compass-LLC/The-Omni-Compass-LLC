# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 32.7 | 44.9 | +37.1% | -11.5 to 35.8 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 984 | 984 | -0.0% | -6.94 to 6.14 | STEADY, no difference beyond the noise |
| queries a second | 984 | 984 | -0.0% | -6.94 to 6.14 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.46 | 1.38 | -5.9% | -0.321 to 0.147 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.38 | 2.17 | -8.5% | -0.602 to 0.198 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.938 | 0.906 | -3.4% | -0.131 to 0.068 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.3% | 700 to 747 | power given |
| pages holding data, mean (MB) | 456 | 888 | +94.5% | 404 to 458 | power given |
| pages read from disk into the pool (misses) | 192,406 | 71,780 | -62.7% | -128,650 to -112,602 | shown, not judged |
| host CPU busy (share of the run) | 0.223 | 0.213 | -4.5% | -0.0376 to 0.0175 | STEADY, no difference beyond the noise |
| host CPU-seconds | 392 | 374 | -4.5% | -65.5 to 30.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 26.7 | 18.4 | -31.4% | -26 to 9.22 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
