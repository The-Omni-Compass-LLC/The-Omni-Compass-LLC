# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 17.7 | 28.4 | +60.2% | 8.16 to 13.2 | GAIN |
| throughput (transactions a second) | 984 | 984 | +0.1% | -3 to 4.38 | STEADY, no difference beyond the noise |
| queries a second | 984 | 984 | +0.1% | -3 to 4.38 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.96 | 1.6 | -18.5% | -0.514 to -0.212 | GAIN |
| latency, 99th percentile (ms) | 3.13 | 2.74 | -12.4% | -0.685 to -0.0894 | GAIN |
| latency, mean (ms) | 1.07 | 0.992 | -7.2% | -0.141 to -0.014 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,282 | +901.6% | 1,083 to 1,225 | power given |
| pages holding data, mean (MB) | 118 | 871 | +639.2% | 726 to 780 | power given |
| pages read from disk into the pool (misses) | 417,474 | 78,014 | -81.3% | -354,510 to -324,409 | shown, not judged |
| host CPU busy (share of the run) | 0.26 | 0.231 | -10.9% | -0.0511 to -0.00528 | GAIN |
| host CPU-seconds | 455 | 406 | -10.9% | -88.4 to -10.7 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 56.7 | 31.4 | -44.6% | -39 to -11.5 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
