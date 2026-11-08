# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,946 | 2,943 | -0.1% | -17.5 to 12 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,954 | 2,953 | -0.1% | -18.7 to 15.5 | STEADY, no difference beyond the noise |
| queries a second | 2,954 | 2,953 | -0.1% | -18.7 to 15.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.342 | 0.336 | -1.8% | -0.0209 to 0.00891 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.473 | 0.478 | +1.2% | -0.0187 to 0.0301 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.204 | 0.199 | -2.6% | -0.0123 to 0.00181 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 508 | +296.8% | -3.71 to 764 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 475 | +292.1% | 3.32 to 705 | power given |
| pages read from disk into the pool (misses) | 1,031,283 | 399,609 | -61.3% | -1,015,347 to -248,000 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.16 | -2.4% | -0.00814 to 0.000197 | STEADY, no difference beyond the noise |
| host CPU-seconds | 289 | 282 | -2.4% | -13.6 to -0.358 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 0.214 | 0.209 | -2.3% | -0.0105 to 0.000538 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.67 |  | -1.2 to 4.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
