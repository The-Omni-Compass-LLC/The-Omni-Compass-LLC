# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 194 | 194 | -0.1% | -11 to 10.8 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 198 | 197 | -0.3% | -5.58 to 4.31 | STEADY, no difference beyond the noise |
| queries a second | 3,959 | 3,947 | -0.3% | -112 to 86.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.24 | 5.62 | -10.0% | -4.38 to 3.14 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 17.4 | 13.6 | -21.9% | -27.6 to 19.9 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.27 | 2.96 | -9.4% | -0.719 to 0.104 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,076 | +110.1% | 110 to 1,018 | power given |
| pages holding data, mean (MB) | 464 | 907 | +95.5% | 144 to 742 | power given |
| pages read from disk into the pool (misses) | 618,726 | 187,509 | -69.7% | -580,557 to -281,877 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.132 | -6.5% | -0.0386 to 0.0202 | STEADY, no difference beyond the noise |
| host CPU-seconds | 250 | 234 | -6.5% | -68.1 to 35.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.83 | 2.65 | -6.4% | -0.616 to 0.251 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.67 |  | -4.37 to 15.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
