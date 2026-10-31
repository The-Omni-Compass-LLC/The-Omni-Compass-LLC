# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 196 | +2.7% | 3.51 to 6.9 | GAIN |
| throughput (transactions a second) | 196 | 197 | +0.3% | -0.639 to 1.78 | EVEN, no difference beyond the noise |
| queries a second | 3,924 | 3,936 | +0.3% | -12.8 to 35.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.11 | 7.08 | -22.3% | -2.44 to -1.62 | GAIN |
| latency, 99th percentile (ms) | 13.5 | 9.68 | -28.5% | -5.65 to -2.08 | GAIN |
| latency, mean (ms) | 5.38 | 5.09 | -5.4% | -0.623 to 0.0404 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,106 | +115.9% | 521 to 666 | power given |
| pages holding data, mean (MB) | 462 | 976 | +111.0% | 431 to 595 | power given |
| pages read from disk into the pool (misses) | 615,929 | 99,113 | -83.9% | -585,405 to -448,228 | shown, not judged |
| host CPU busy (share of the run) | 0.282 | 0.266 | -5.8% | -0.0222 to -0.0107 | GAIN |
| host CPU-seconds | 496 | 467 | -5.9% | -39.1 to -19.3 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.69 | 5.21 | -8.4% | -0.554 to -0.401 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 5.67 |  | 4.23 to 7.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
