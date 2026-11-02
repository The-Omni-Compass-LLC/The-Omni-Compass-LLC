# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 169 | 212 | +25.3% | -7.5 to 93.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 989 | 988 | -0.0% | -6.94 to 6.47 | STEADY, no difference beyond the noise |
| queries a second | 989 | 988 | -0.0% | -6.94 to 6.47 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 66.1 | 31.8 | -51.8% | -304 to 235 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 218 | 162 | -25.7% | -682 to 570 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 11.4 | 7.02 | -38.5% | -41.1 to 32.3 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,271 | +892.6% | 1,053 to 1,232 | power given |
| pages holding data, mean (MB) | 118 | 884 | +648.4% | 760 to 771 | power given |
| pages read from disk into the pool (misses) | 418,743 | 71,024 | -83.0% | -363,569 to -331,868 | shown, not judged |
| host CPU busy (share of the run) | 0.166 | 0.143 | -13.9% | -0.0277 to -0.0186 | GAIN |
| host CPU-seconds | 291 | 251 | -13.9% | -48.8 to -32.3 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.93 | 2.64 | -32.8% | -2.88 to 0.306 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
