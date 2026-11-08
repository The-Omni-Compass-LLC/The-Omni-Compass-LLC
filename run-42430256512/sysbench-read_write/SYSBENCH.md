# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 177 | 188 | +6.0% | -1.31 to 22.6 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 198 | 197 | -0.3% | -0.811 to -0.349 | LOSS |
| queries a second | 3,957 | 3,945 | -0.3% | -16.2 to -6.98 | LOSS |
| latency, 95th percentile (ms) | 42.3 | 11.1 | -73.8% | -95.6 to 33.1 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 281 | 89.5 | -68.2% | -474 to 91 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 13.7 | 6.72 | -50.9% | -16.5 to 2.56 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,229 | +859.8% | 1,032 to 1,169 | power given |
| pages holding data, mean (MB) | 121 | 1,011 | +736.8% | 848 to 933 | power given |
| pages read from disk into the pool (misses) | 1,672,169 | 96,814 | -94.2% | -1,664,677 to -1,486,033 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.168 | -17.6% | -0.0401 to -0.0319 | GAIN |
| host CPU-seconds | 361 | 298 | -17.6% | -71.1 to -56.1 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.48 | 3.48 | -22.3% | -1.34 to -0.648 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 14 |  | 9.03 to 19 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
