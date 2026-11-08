# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 293 | -0.5% | -6.88 to 3.91 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 293 | -0.5% | -6.73 to 3.68 | STEADY, no difference beyond the noise |
| queries a second | 4,716 | 4,692 | -0.5% | -108 to 58.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.85 | 4.74 | -2.4% | -0.24 to 0.00981 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.79 | 6.59 | -3.0% | -0.371 to -0.0294 | GAIN |
| latency, mean (ms) | 3.15 | 3.11 | -1.3% | -0.0985 to 0.0157 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 712 | +39.0% | 198 to 202 | power given |
| pages holding data, mean (MB) | 451 | 642 | +42.3% | 188 to 194 | power given |
| pages read from disk into the pool (misses) | 247,487 | 181,007 | -26.9% | -70,155 to -62,805 | shown, not judged |
| host CPU busy (share of the run) | 0.247 | 0.242 | -2.0% | -0.0086 to -0.00115 | GAIN |
| host CPU-seconds | 147 | 144 | -2.1% | -4.68 to -1.44 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.27 | 3.22 | -1.5% | -0.0764 to -0.0214 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
