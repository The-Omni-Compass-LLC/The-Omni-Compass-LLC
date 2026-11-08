# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 92.3 | 102 | +10.6% | -54.6 to 74.2 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 981 | 979 | -0.2% | -6.81 to 3.25 | STEADY, no difference beyond the noise |
| queries a second | 981 | 979 | -0.2% | -6.81 to 3.25 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.31 | 1.27 | -2.7% | -0.289 to 0.219 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.01 | 1.93 | -3.9% | -0.694 to 0.539 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.876 | 0.86 | -1.8% | -0.128 to 0.0959 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.4% | 700 to 747 | power given |
| pages holding data, mean (MB) | 456 | 889 | +95.0% | 405 to 461 | power given |
| pages read from disk into the pool (misses) | 190,232 | 71,848 | -62.2% | -129,221 to -107,547 | shown, not judged |
| host CPU busy (share of the run) | 0.21 | 0.204 | -2.8% | -0.0384 to 0.0267 | STEADY, no difference beyond the noise |
| host CPU-seconds | 382 | 371 | -2.8% | -69.3 to 48.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 9.85 | 8.04 | -18.4% | -11.8 to 8.21 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
