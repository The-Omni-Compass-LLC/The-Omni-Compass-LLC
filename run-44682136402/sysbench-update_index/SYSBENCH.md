# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 33.3 | 39.1 | +17.3% | -4.86 to 16.4 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 985 | 985 | -0.0% | -5.95 to 5.08 | STEADY, no difference beyond the noise |
| queries a second | 985 | 985 | -0.0% | -5.95 to 5.08 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.5 | 1.45 | -3.2% | -0.314 to 0.218 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.59 | 2.48 | -4.3% | -0.505 to 0.28 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.954 | 0.939 | -1.6% | -0.0931 to 0.0627 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,235 | +141.3% | 704 to 743 | power given |
| pages holding data, mean (MB) | 459 | 888 | +93.6% | 417 to 442 | power given |
| pages read from disk into the pool (misses) | 187,818 | 71,932 | -61.7% | -134,707 to -97,065 | shown, not judged |
| host CPU busy (share of the run) | 0.23 | 0.227 | -1.4% | -0.0306 to 0.0244 | STEADY, no difference beyond the noise |
| host CPU-seconds | 403 | 398 | -1.3% | -53.1 to 42.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 27.8 | 22.4 | -19.3% | -21.9 to 11.2 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
