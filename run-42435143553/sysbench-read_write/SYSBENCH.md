# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 181 | 184 | +1.6% | -4.26 to 10 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 198 | 198 | +0.1% | -1.07 to 1.65 | STEADY, no difference beyond the noise |
| queries a second | 3,951 | 3,957 | +0.1% | -21.5 to 32.9 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 26.8 | 26.2 | -2.4% | -12.6 to 11.3 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 169 | 119 | -29.6% | -114 to 14.3 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 9.87 | 8.27 | -16.3% | -3.81 to 0.604 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,232 | +140.7% | 679 to 762 | power given |
| pages holding data, mean (MB) | 463 | 1,021 | +120.7% | 538 to 579 | power given |
| pages read from disk into the pool (misses) | 619,704 | 91,266 | -85.3% | -572,870 to -484,006 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.17 | -8.7% | -0.0201 to -0.0122 | GAIN |
| host CPU-seconds | 329 | 301 | -8.7% | -35 to -22.2 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.98 | 3.58 | -10.1% | -0.454 to -0.35 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 4.87 to 12.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 8.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
