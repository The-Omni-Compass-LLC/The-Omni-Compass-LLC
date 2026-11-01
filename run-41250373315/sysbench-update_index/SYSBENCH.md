# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 225 | 275 | +22.1% | -125 to 225 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 989 | 988 | -0.1% | -3.68 to 1.04 | STEADY, no difference beyond the noise |
| queries a second | 989 | 988 | -0.1% | -3.68 to 1.04 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.7 | 4.16 | -11.5% | -6.69 to 5.6 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.7 | 12.7 | +0.4% | -21.3 to 21.4 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.49 | 1.41 | -5.2% | -1.23 to 1.08 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,224 | +139.1% | 649 to 775 | power given |
| pages holding data, mean (MB) | 454 | 887 | +95.3% | 404 to 462 | power given |
| pages read from disk into the pool (misses) | 192,114 | 71,492 | -62.8% | -127,681 to -113,561 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.109 | -6.3% | -0.0307 to 0.0162 | STEADY, no difference beyond the noise |
| host CPU-seconds | 204 | 191 | -6.2% | -53.7 to 28.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.04 | 1.57 | -23.1% | -2.25 to 1.31 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
