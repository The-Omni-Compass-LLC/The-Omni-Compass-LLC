# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 297 | 296 | -0.3% | -2.3 to 0.707 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.2% | -1.85 to 0.643 | STEADY, no difference beyond the noise |
| queries a second | 4,753 | 4,744 | -0.2% | -29.5 to 10.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.65 | 1.64 | -0.4% | -0.162 to 0.148 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.13 | 3.36 | +7.2% | -0.984 to 1.43 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.15 | 1.16 | +0.7% | -0.0873 to 0.103 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 688 | +34.3% | -204 to 555 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 610 | +31.4% | -175 to 466 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,962 | 447,010 | -31.9% | -661,443 to 243,538 | shown, not judged |
| host CPU busy (share of the run) | 0.0937 | 0.0935 | -0.2% | -0.0022 to 0.0019 | STEADY, no difference beyond the noise |
| host CPU-seconds | 168 | 168 | -0.1% | -3.99 to 3.52 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.25 | 1.25 | +0.1% | -0.0333 to 0.0361 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | -4.92 to 10.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
