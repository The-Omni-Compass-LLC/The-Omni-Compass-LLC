# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 178 | 241 | +35.6% | -47.1 to 173 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 987 | 988 | +0.1% | -0.664 to 2.79 | STEADY, no difference beyond the noise |
| queries a second | 987 | 988 | +0.1% | -0.664 to 2.79 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.31 | 4.35 | +31.5% | -3.84 to 5.92 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 14.9 | 13.1 | -11.7% | -18.1 to 14.6 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.41 | 1.75 | +23.7% | -0.7 to 1.37 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,301 | +916.4% | 1,169 to 1,177 | power given |
| pages holding data, mean (MB) | 118 | 881 | +646.2% | 756 to 770 | power given |
| pages read from disk into the pool (misses) | 415,318 | 70,880 | -82.9% | -358,443 to -330,433 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.114 | -17.4% | -0.0494 to 0.00138 | STEADY, no difference beyond the noise |
| host CPU-seconds | 242 | 200 | -17.4% | -86.4 to 2.09 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.14 | 1.84 | -41.4% | -3.71 to 1.11 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
