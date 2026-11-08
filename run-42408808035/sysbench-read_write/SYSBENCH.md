# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 188 | 189 | +0.7% | -7.48 to 10.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.1% | -3.59 to 3.14 | STEADY, no difference beyond the noise |
| queries a second | 3,943 | 3,938 | -0.1% | -71.8 to 62.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 12.2 | 6.97 | -42.7% | -20.3 to 9.92 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 605 | 108 | -82.1% | -2,414 to 1,421 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 17.3 | 6.64 | -61.7% | -50.1 to 28.7 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,156 | +125.7% | 439 to 849 | power given |
| pages holding data, mean (MB) | 462 | 977 | +111.4% | 390 to 640 | power given |
| pages read from disk into the pool (misses) | 618,720 | 125,056 | -79.8% | -568,474 to -418,854 | shown, not judged |
| host CPU busy (share of the run) | 0.183 | 0.17 | -6.9% | -0.0203 to -0.0049 | GAIN |
| host CPU-seconds | 324 | 302 | -6.8% | -35.3 to -8.54 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.78 | 3.5 | -7.4% | -0.528 to -0.0326 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | -0.606 to 16.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
